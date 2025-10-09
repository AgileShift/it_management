from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from it_management.it_management.doctype.employee_device.employee_device import EmployeeDevice
		from it_management.it_management.doctype.employee_email.employee_email import EmployeeEmail
		from it_management.it_management.doctype.employee_sim.employee_sim import EmployeeSIM

		active: DF.Check
		assigned_devices: DF.Table[EmployeeDevice]
		assigned_emails: DF.Table[EmployeeEmail]
		assigned_sims: DF.Table[EmployeeSIM]
		branch: DF.Link
		company: DF.Literal["Distribuidora Reyes NIC", "Distribuidora Reyes CR", "Transporte Reyes", "Kings Exports Imports", "Grupo Reyes"]
		department: DF.Link
		designation: DF.Literal["Abogado", "Analista", "Asistente Gerencia", "Auditor", "Auxiliar de Bodega", "Cajero", "Cajero y Facturador", "Cajero\\Liquidador", "Cartera y Cobro", "Vendedor", "Vendedor en Ruta", "Compras", "Contador", "Contador Rotativo", "Ejecutivo de Venta", "Importaciones", "Jefe de Area", "Liquidador", "Reponsable de Modulo", "Responsable de Bodega", "RRHH", "Soporte Tecnico", "Supervisor", "Supervisor de Ruta", "Supervisor de CEDI", "Supervisor de Modulo", "Mecanico Frio", "Mecanico General", "Mecanico Electrico", "Diseno Grafico"]
		first_name: DF.Data
		gender: DF.Link | None
		last_name: DF.Data
		middle_name: DF.Data | None
		personal_email: DF.Data | None
		personal_phone: DF.Phone | None
		reports_to: DF.Link | None
	# end: auto-generated types
	pass
