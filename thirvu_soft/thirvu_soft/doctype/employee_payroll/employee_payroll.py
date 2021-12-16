# Copyright (c) 2021, Gokul and contributors
# For license information, please see license.txt

# =import frappe
from frappe.model.document import Document

class employee_payroll(Document):
	 def validate(self):
		 r={"Developer":1000, "Tech lead":30000, "House keeping":9000, "Intern":8100, "HR":40000}
		 self.basic_pay=r[self.emp_role]
		 self.pf=8.5

