from fpdf import FPDF
from employee_manager import EmployeeManager

title = 'Salary Slip'

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)

        w = self.get_string_width(title)+6
        self.set_x((210-w)/2)

        self.set_fill_color(57, 230, 0)
        self.set_text_color(220, 50, 50)

        self.set_line_width(1)

        self.cell(w, 9, title, 1, 1, 'C', 1)

        self.ln(10)

    def salary_title(self, employee_id, designation):
        self.set_font('Arial', 'I', 8)
        self.set_fill_color(200, 220, 225)
        self.cell(0, 6, 'Employee Id: %d | Department: %s' %(employee_id, designation), 0, 1, 'L', 1)
        self.ln(4)
    
    def salary_body(self, employee_id):
        employee_obj = EmployeeManager()
        employee = employee_obj.get_employee(employee_id)
        employee_first_name = employee.first_name
        employee_last_name = employee.last_name
        employee_department = employee.department
        employee_salary = employee.salary

        self.set_font('Times', '', 18)
        self.cell(0, 10, "Employee Name: " + str(employee_first_name) + " " + str(employee_last_name), 0, 1)
        self.cell(0, 10, "Employee Department: " + str(employee_department), 0, 1)
        
        self.ln(2)
        self.set_font('Times', '', 22)
        self.cell(0, 10, "Salary " + str(employee_salary), 0, 1)
    
    def print_pdf(self, employee_id):
        employee_obj = EmployeeManager()
        employee = employee_obj.get_employee(employee_id)
        employee_designation = employee.designation
        self.add_page()
        self.salary_title(employee_id, employee_designation)
        self.salary_body(employee_id)







        


