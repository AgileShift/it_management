import frappe
from frappe.model.document import Document


class Email(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data
		forward_to: DF.Link | None
		password: DF.Password | None
		type: DF.Literal["Email", "Alias", "Forwarder"]
	# end: auto-generated types

	@frappe.whitelist(allow_guest=False)
	def get_password(self):
		return super().get_password()
