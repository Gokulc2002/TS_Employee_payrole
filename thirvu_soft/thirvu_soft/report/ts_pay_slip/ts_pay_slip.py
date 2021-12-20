# Copyright (c) 2013, Gokul and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	filters=frappe._dict(filters or {})
	columns= get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	Columns =[
		{
			"label":_("EMP ID"),
			"fieldname":"emp_id",
			"fieldtype":"Data",
			
		},
		{
			"label":_("Name"),
			"fieldname":"emp_name",
			"fieldtype":"Data"
		},
		{
			"label":_("Start Date"),
			"fieldname":"start_date",
			"fieldtype":"Date"
		},
		{
			"label":_("Last Date"),
			"fieldname":"last_date",
			"fieldtype":"Date"
		}
		
	]
	return Columns
def get_conditions(filters):
	conditions= {}
	
	if filters.start_date:
		conditions["start_date"] = filters.start_date


	if filters.last_date:
		conditions["last_date"] = filters.last_date
	print(conditions,filters.start_date, filters.last_date)
	return conditions


def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	emp = frappe.db.get_all("employee_payroll", fields=["emp_id", "emp_name", "start_date", "last_date"],
		filters=conditions, order_by='emp_id')
	for d in emp:	
		row = {"emp_id" : d.emp_id, "emp_name":d.emp_name, "start_date": d.start_date, "last_date": d.last_date}
		data.append(row)
	return data
