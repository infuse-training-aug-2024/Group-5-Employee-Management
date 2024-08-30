class Payroll:
    def __init__(self, employee_id: int, base_salary: float):
        self.employee_id= employee_id
        self.base_salary = base_salary
        self.deductions = 0
        self.bonuses = 0
        self.total_salary=0

    def calculate_total(self, leaves: int, performance: int):
        try:
            if leaves < 0:
                self.deductions = 0.10 * self.base_salary
            else:
                self.deductions = 0
            if performance==5:
                self.bonuses = 0.10 * self.base_salary
            elif performance==4:
                self.bonuses = 0.05 * self.base_salary
            elif performance>1 and performance<=3:
                self.bonuses = 0.02 * self.base_salary
            
            total_salary = self.base_salary - self.deductions + self.bonuses
            print(total_salary)
        except ValueError as v:
            print(f"Input Error: {v}")
        except Exception as e:
            print(f"Exception occured: {e}")
obj=Payroll(121,50000)
obj.calculate_total(0,3)
