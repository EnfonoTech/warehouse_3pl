"""Force the Warehouse 3PL workspace to pick up shortcut changes.

A plain `bench migrate` does not overwrite a Workspace record that already exists in the
site database, so shipping a new shortcut in the app's workspace JSON has no effect on any
site where the app is already installed -- it silently keeps the old shortcut list. The
reload has to be forced.
"""

import frappe


def execute():
	if not frappe.db.exists("Workspace", "Warehouse 3PL"):
		return
	frappe.reload_doc("warehouse_3pl", "workspace", "warehouse_3pl", force=True)
