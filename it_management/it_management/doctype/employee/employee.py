import vobject

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
		company: DF.Literal["", "Distribuidora Reyes NIC", "Distribuidora Reyes CR", "Transporte Reyes", "Kings Exports Imports", "Grupo Reyes"]
		department: DF.Link
		designation: DF.Literal["Abogado", "Analista", "Asistente Gerencia", "Auditor", "Asistente de Area", "Auxiliar de Bodega", "Cajero", "Facturador", "Cajero y Facturador", "Cajero\\Liquidador", "Cartera y Cobro", "Vendedor", "Vendedor en Ruta", "Compras", "Contador", "Contador Rotativo", "Ejecutivo de Venta", "Importaciones", "Jefe de Area", "Liquidador", "Reponsable de Modulo", "Responsable de Bodega", "RRHH", "Soporte Tecnico", "Supervisor", "Supervisor de Ruta", "Supervisor de CEDI", "Supervisor de Modulo", "Mecanico Frio", "Mecanico General", "Mecanico Electrico", "Diseno Grafico"]
		first_name: DF.Data
		gender: DF.Link | None
		last_name: DF.Data
		personal_email: DF.Data | None
		personal_phone: DF.Data | None
		reports_to: DF.Link | None
	# end: auto-generated types

	def vcard(self):
		card = vobject.vCard()
		card.add('n')
		card.n.value = vobject.vcard.Name(given=self.first_name, family=self.last_name)
		card.add('fn')
		card.fn.value = f"{self.first_name} {self.last_name}"

		card.add('title').value = self.designation # Job Title
		card.add('org').value = [self.company, self.department]

		# TODO: Make this a optional setting
		if self.personal_phone:
			card_tel = card.add('tel')
			card_tel.value = self.personal_phone
			card_tel.type_param = 'MOBILE'

		for employee_email in self.assigned_emails:
			card_email = card.add('email')
			card_email.value = employee_email.email
			card_email.type_param = 'WORK'

		for employee_sim in self.assigned_sims:
			card_tel = card.add('tel')
			card_tel.value = employee_sim.sim
			card_tel.type_param = 'WORK'

		return card.serialize()

