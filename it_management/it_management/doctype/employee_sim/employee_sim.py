# Copyright (c) 2025, Agile Shift I/O and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeeSIM(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		call: DF.ReadOnly | None
		data: DF.ReadOnly | None
		data_plan: DF.ReadOnly | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		sim: DF.Link
	# end: auto-generated types
	pass
