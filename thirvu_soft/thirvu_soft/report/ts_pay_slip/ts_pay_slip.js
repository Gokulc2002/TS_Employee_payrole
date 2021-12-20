// Copyright (c) 2016, Gokul and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Pay Slip"] = {
	"filters": [

	{
		label: __("Start Date"),
		fieldname:("start_date"),
		fieldtype:"Date",
		reqd:1
	},
	{
		label: __("Last Date"),
		fieldname:("last_date"),
		fieldtype:"Date",
		reqd:1
	}
	]
};
