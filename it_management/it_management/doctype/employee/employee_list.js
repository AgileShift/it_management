frappe.listview_settings['Employee'] = {
	hide_name_filter: true,
	hide_name_column: true,
	add_fields: ['active'],

	filters: [
		['active', '=', 1]
	],
}
