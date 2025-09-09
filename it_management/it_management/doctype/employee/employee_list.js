frappe.listview_settings['Employee'] = {
	hide_name_filter: true,
	add_fields: ['active'],

	filters: [
		['active', '=', 1]
	],
}
