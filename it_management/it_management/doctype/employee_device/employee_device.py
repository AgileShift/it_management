from frappe.model.document import Document


class EmployeeDevice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		device: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		serial_no: DF.ReadOnly | None
		type: DF.ReadOnly | None
	# end: auto-generated types
	pass
