import frappe
@frappe.whitelist(allow_guest=True)
def spark():
    a=frappe.get_all("TS Customer_Details")
    return a
 