from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from it_management.it_management.doctype.employee_email.employee_email import EmployeeEmail

		active: DF.Check
		assigned_emails: DF.Table[EmployeeEmail]
		branch: DF.Link
		company: DF.Literal["Distribuidora Reyes NIC", "Distribuidora Reyes CR", "Transporte Reyes", "Kings Exports Imports", "Grupo Reyes"]
		department: DF.Link
		designation: DF.Literal["Contador", "Auxiliar Contable", "Vendedor", "Jefe de Area", "Supervisor"]
		first_name: DF.Data
		gender: DF.Link | None
		last_name: DF.Data
		middle_name: DF.Data | None
		personal_email: DF.Data | None
		personal_phone: DF.Phone | None
		reports_to: DF.Link | None
	# end: auto-generated types
