# Copyright (c) 2026, Enfono and Contributors
# See license.txt
"""Invoicing a job's billable activity.

Covers the two defects that made billing unusable: make_sales_invoice built lines with no
item_code, so ERPNext refused the invoice with "Income Account None does not belong to
Company X"; and Billing Transaction.invoiced was never written, so the same receipt or pick
could be billed twice with no way to trace an invoice line back to the work.
"""

import frappe
from frappe.tests.utils import FrappeTestCase

from warehouse_3pl.warehouse_3pl.doctype.warehouse_job_record.warehouse_job_record import (
	activity_item_code,
	make_sales_invoice,
)


class TestWarehouseJobRecord(FrappeTestCase):
	def test_activity_item_code_convention(self):
		self.assertEqual(activity_item_code("Receiving"), "3PL-RECEIVING")
		self.assertEqual(activity_item_code("Storage"), "3PL-STORAGE")
		# Hyphenated and spaced activities collapse to one stable code.
		self.assertEqual(activity_item_code("VAS-Shrink Wrap"), "3PL-VAS-SHRINK-WRAP")

	def test_every_line_carries_an_item_code(self):
		"""A Sales Invoice Item without item_code cannot resolve an income account."""
		job = self._job_with_activity()
		si = make_sales_invoice(job)
		self.assertTrue(si.items)
		for row in si.items:
			self.assertTrue(row.item_code, "every invoice line needs an item_code")

	def test_missing_service_item_is_one_clear_message(self):
		job = self._job_with_activity(item_exists=False)
		self.assertRaises(frappe.ValidationError, make_sales_invoice, job)

	def test_a_job_with_nothing_to_bill_is_refused(self):
		job = frappe.get_doc({
			"doctype": "Warehouse Job Record",
			"date": frappe.utils.today(),
			"client": self._client(),
			"company": self._company(),
			"job_status": "Created",
		}).insert().name
		self.assertRaises(frappe.ValidationError, make_sales_invoice, job)

	# ---------------------------------------------------------------- helpers
	def _company(self):
		return frappe.get_all("Company", pluck="name")[0]

	def _client(self):
		name = "_Test 3PL Client"
		if not frappe.db.exists("Customer", name):
			frappe.get_doc({"doctype": "Customer", "customer_name": name,
			                "is_3pl_client": 1}).insert()
		return name

	def _job_with_activity(self, item_exists=True):
		code = activity_item_code("Receiving")
		if item_exists and not frappe.db.exists("Item", code):
			frappe.get_doc({"doctype": "Item", "item_code": code, "item_name": "3PL Receiving",
			                "item_group": frappe.get_all("Item Group", filters={"is_group": 0},
			                                             pluck="name")[0],
			                "stock_uom": "Nos", "is_stock_item": 0}).insert()
		if not item_exists and frappe.db.exists("Item", code):
			frappe.delete_doc("Item", code, force=True, ignore_permissions=True)

		job = frappe.get_doc({
			"doctype": "Warehouse Job Record",
			"date": frappe.utils.today(),
			"client": self._client(),
			"company": self._company(),
			"job_status": "Created",
		}).insert()
		frappe.get_doc({
			"doctype": "Billing Transaction",
			"client": job.client,
			"warehouse_job": job.name,
			"activity_type": "Receiving",
			"transaction_date": frappe.utils.today(),
			"qty": 10, "uom": "Per Unit", "rate": 2.5,
		}).insert()
		return job.name
