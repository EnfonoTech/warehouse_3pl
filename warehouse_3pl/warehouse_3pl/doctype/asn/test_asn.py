# Copyright (c) 2026, Enfono and Contributors
# See license.txt
"""ASN -> Receiving mapping.

Guards the defect where a Receiving created from an ASN inherited the ASN's
naming_series and came out named ASN-2026-000NN, sharing one number sequence with
advance notices and making the two indistinguishable by name.
"""

import frappe
from frappe.tests.utils import FrappeTestCase

from warehouse_3pl.warehouse_3pl.doctype.asn.asn import make_receiving


class TestASN(FrappeTestCase):
	def test_naming_series_is_marked_no_copy_on_every_series_doctype(self):
		"""Frappe's mapper copies any same-named field not marked no_copy."""
		for doctype in ("ASN", "Receiving", "Client Order", "Wave", "Pick Task",
		                "Pack Task", "Putaway Task", "Warehouse Job Record",
		                "Billing Transaction"):
			field = frappe.get_meta(doctype).get_field("naming_series")
			if not field:
				continue
			self.assertTrue(
				field.no_copy,
				f"{doctype}.naming_series must be no_copy, or a mapper will carry it across",
			)

	def test_mapper_does_not_carry_the_asn_series_onto_the_receiving(self):
		no_map = self._field_no_map()
		for fieldname in ("naming_series", "amended_from", "status"):
			self.assertIn(fieldname, no_map)

	def _field_no_map(self):
		"""Read the mapping table make_receiving() passes to get_mapped_doc."""
		captured = {}

		def fake_get_mapped_doc(from_doctype, from_docname, table_maps, target_doc=None, **kwargs):
			captured.update(table_maps)
			return frappe.new_doc("Receiving")

		import frappe.model.mapper as mapper
		original = mapper.get_mapped_doc
		mapper.get_mapped_doc = fake_get_mapped_doc
		try:
			make_receiving("dummy")
		except Exception:
			pass
		finally:
			mapper.get_mapped_doc = original

		return captured.get("ASN", {}).get("field_no_map", [])
