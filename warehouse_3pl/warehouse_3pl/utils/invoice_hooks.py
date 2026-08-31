"""Keep Billing Transactions in step with the Sales Invoice raised from a job.

Billing Transaction carries `invoiced` and `sales_invoice` fields, but nothing ever wrote
them: an activity could be invoiced twice and no invoice line could be traced back to the
receipt or the pick that produced it. make_sales_invoice() now only picks up uninvoiced
transactions, and these hooks are what make that filter mean anything.
"""

import frappe


def mark_billing_transactions_invoiced(doc, method=None):
    """On submit, stamp every billing transaction this invoice covers."""
    job = doc.get("custom_warehouse_job")
    if not job:
        return
    names = frappe.get_all(
        "Billing Transaction",
        filters={"warehouse_job": job, "invoiced": 0},
        pluck="name",
    )
    for name in names:
        frappe.db.set_value(
            "Billing Transaction", name, {"invoiced": 1, "sales_invoice": doc.name},
            update_modified=False,
        )


def release_billing_transactions(doc, method=None):
    """On cancel, release them so the work can be invoiced again."""
    job = doc.get("custom_warehouse_job")
    if not job:
        return
    names = frappe.get_all(
        "Billing Transaction",
        filters={"warehouse_job": job, "sales_invoice": doc.name},
        pluck="name",
    )
    for name in names:
        frappe.db.set_value(
            "Billing Transaction", name, {"invoiced": 0, "sales_invoice": None},
            update_modified=False,
        )
