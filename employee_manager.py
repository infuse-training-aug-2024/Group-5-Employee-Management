from employee_record import Employee
import numpy as np
from typing import List

class EmployeeManager:
    def __init__(self):
        data = np.genfromtxt('employee_data.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')
        self.employees: List[Employee] = []
        for row in data:
            employee = Employee(
                employee_id=int(row['emp_id']),
                first_name=row['firstname'],
                last_name=row['lastname'],
                department=row['department'],
                salary=float(row['salary']),
                designation=row['designation'],
                attendance=int(row['attendance']),
                performance=int(row['performance'])
            )
            self.employees.append(employee)

        for employee in self.employees:
            print(employee.employee_id)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id: int):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def get_employee(self, employee_id: int) -> Employee:
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def list_employees(self) -> List[Employee]:
        return self.employees


employeemanager = EmployeeManager()
