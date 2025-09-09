from frappe.model.document import Document


class Email(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data
		password: DF.Password | None
		type: DF.Literal["Email", "Alias", "Forwarder"]
	# end: auto-generated types
