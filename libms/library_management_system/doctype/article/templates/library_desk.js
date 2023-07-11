// Copyright (c) 2023, Diya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Article", {
  refresh: function (frm) {
    frm.add_custom_button("Add New Book", function () {
      frappe.new_doc("Article");
    });
  }
});

