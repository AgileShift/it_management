frappe.listview_settings['Employee'] = {
	add_fields: ['active'],

	filters: [
		['active', '=', 1]
	],

	formatters: {
		active: (value) => value ? 'Si' : 'No', // TODO: Complete this
    }

}
