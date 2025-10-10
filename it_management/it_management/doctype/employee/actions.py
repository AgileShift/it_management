import frappe


@frappe.whitelist(allow_guest=False)
def download_vcard(employee: str):
	employee = frappe.get_doc("Employee", employee)
	vcard = employee.vcard()
	frappe.local.response.filename = f"{employee.first_name}_{employee.last_name}.vcf"
	frappe.local.response.filecontent = vcard
	frappe.local.response.type = "download"
