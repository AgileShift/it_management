from frappe.model.document import Document


class SIM(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		call: DF.Data | None
		company: DF.Literal["", "Distribuidora Reyes NIC", "Distribuidora Reyes CR", "Transporte Reyes", "Kings Exports Imports", "Grupo Reyes"]
		cost_usd: DF.Currency
		data: DF.Data | None
		data_plan: DF.Data | None
		extra_data: DF.Data | None
		sim: DF.Data
		sms: DF.Data | None
		social_network: DF.Data | None
		vpn: DF.Data | None
	# end: auto-generated types
	pass
