"""Controller for the in-ERP Warehouse 3PL operating guide.

The filename MUST stay underscored. A hyphen is not a valid Python module name, so
Frappe cannot import the controller, skips it without logging anything, and serves the
page to anonymous requests with a 200 -- the guard below never runs. The pretty URL
comes from website_route_rules in hooks.py instead.
"""

import frappe
from frappe import _

no_cache = 1


def get_context(context):
	# Operational documentation naming real clients and rates. Signed-in users only.
	if frappe.session.user == "Guest":
		frappe.throw(_("Please sign in to view the warehouse guide."), frappe.PermissionError)

	context.no_cache = 1
	context.show_sidebar = False
	context.title = _("Warehouse Operating Guide")

	context.storage_rate = _active_storage_rate()
	context.clients = frappe.get_all(
		"Customer",
		filters={"is_3pl_client": 1},
		fields=["name", "client_code", "client_status", "active_rate_card"],
		order_by="client_code",
	)
	context.locations = frappe.get_all(
		"Warehouse Location",
		fields=["name", "warehouse", "status", "max_volume_cbm"],
		order_by="name",
	)
	context.counts = {
		label: frappe.db.count(doctype)
		for label, doctype in (
			("Advance notices", "ASN"),
			("Receipts", "Receiving"),
			("Putaway tasks", "Putaway Task"),
			("Client orders", "Client Order"),
			("Waves", "Wave"),
			("Pick tasks", "Pick Task"),
			("Pack tasks", "Pack Task"),
			("Billing lines", "Billing Transaction"),
		)
	}
	return context


def _active_storage_rate():
	"""The storage rate any active card is currently carrying, for display only."""
	card = frappe.db.get_value("Rate Card", {"status": "Active"}, "name", order_by="effective_from desc")
	if not card:
		return None
	return frappe.db.get_value(
		"Rate Card Line",
		{"parent": card, "activity_type": "Storage"},
		["rate", "uom"],
		as_dict=True,
	)
