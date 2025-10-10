frappe.ui.form.on("Employee", {
	refresh(frm) {
		frm.add_custom_button("Download vCard", () => {
            window.open(`/api/method/it_management.it_management.doctype.employee.actions.download_vcard?employee=${frm.doc.name}`);
        });
	}
});
