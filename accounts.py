from employee_manager import EmployeeManager
from pdf import PDF

class Payroll:

    def __init__(self, employee_id:int):
        self.employee_id = employee_id
        self.employee_obj = EmployeeManager()
        self.base_salary = self.employee_obj.get_employee_salary(employee_id)
        self.deductions = 0
        self.bonuses = 0
        self.total_salary = 0
        self.payroll_leaves = self.employee_obj.get_employee_available_leaves(self.employee_id)
        self.payroll_performance = self.employee_obj.get_employee_performance(self.employee_id)

    def calculate_total(self):
        try:
            # Check if payroll_leaves is None or a non-convertible value
            if self.payroll_leaves is None or str(self.payroll_leaves).lower() == 'none':
                self.payroll_leaves = 0  # Assign a default value for None
            else:
                self.payroll_leaves = int(self.payroll_leaves)

            # Check if payroll_performance is None or a non-convertible value
            if self.payroll_performance is None or str(self.payroll_performance).lower() == 'none':
                self.payroll_performance = 0  # Assign a default value for None
            else:
                self.payroll_performance = int(self.payroll_performance)

            # Calculate deductions based on leaves
            if self.payroll_leaves < 0:
                self.deductions = 0.10 * self.base_salary
            else:
                self.deductions = 0

            # Calculate bonuses based on performance
            if self.payroll_performance == 5:
                self.bonuses = 0.10 * self.base_salary
            elif self.payroll_performance == 4:
                self.bonuses = 0.05 * self.base_salary
            elif 1 < self.payroll_performance <= 3:
                self.bonuses = 0.02 * self.base_salary

            # Calculate total salary
            total_salary = self.base_salary - self.deductions + self.bonuses
            return  total_salary

        except ValueError as v:
            print(f"Input Error: {v}")
        except Exception as e:
            print(f"Exception occurred: {e}")


    def generate_salary_slip(self):
        title = 'Salary Slip'
        pdf = PDF()
        pdf.set_title(title)
        pdf.print_pdf(self.employee_id)
        pdf.output('SalarySlip.pdf','F')


