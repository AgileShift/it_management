from frappe.model.document import Document


class Device(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		branch: DF.Link | None
		brand: DF.Literal["Dell", "Lenovo", "Samsung", "HP", "Canon"]
		cpu: DF.Data | None
		department: DF.Link | None
		imei: DF.Data | None
		model: DF.Data | None
		note: DF.SmallText | None
		purchase_date: DF.Date | None
		ram: DF.Data | None
		serial_no: DF.Data
		software_version: DF.Data | None
		storage: DF.Data | None
		type: DF.Literal["", "PC", "LAPTOP", "TABLET", "CELULAR", "IMPRESORA", "MONITOR", "USB"]
		warranty_time: DF.Data | None
	# end: auto-generated types
	pass
