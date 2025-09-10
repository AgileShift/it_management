frappe.ui.form.on("Email", {
	refresh(frm) {

		frm.add_custom_button(__('Get Password'), function () {
			frappe.call({
				doc: frm.doc,
				method: 'get_password'
			}).then(r => {
				frappe.msgprint(r);
			})
		}, __("Utilities"));

	}
});
