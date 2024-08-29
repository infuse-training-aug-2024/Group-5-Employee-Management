from datetime import date
from typing import List
import numpy as np

class Leave:
    def __init__(self, leave_id: int, start_date: date, end_date: date, leave_type: str, status: str):
        self.leave_id = leave_id
        self.start_date = start_date
        self.end_date = end_date
        self.type = leave_type
        self.status = status

    def apply_leave(self):
        # Logic to apply for a leave
        pass

class Performance:
    def __init__(self, review_id: int, score: int, feedback: str):
        self.review_id = review_id
        self.score = score
        self.feedback = feedback

    def evaluate(self):
        # Logic to evaluate performance
        pass

class Payroll:
    def __init__(self, payroll_id: int, base_salary: float, deductions: float, bonuses: float):
        self.payroll_id = payroll_id
        self.base_salary = base_salary
        self.deductions = deductions
        self.bonuses = bonuses

    def calculate_total(self) -> float:
        return self.base_salary - self.deductions + self.bonuses

    def generate_payslip(self):
        # Logic to generate a payslip
        pass

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, department: str, salary: float, designation: str , attendance: int, performance: int):
        self.attendance = attendance
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.designation  = designation
        self.salary = salary
        # self.attendance: attendance
        self.performance = performance

    def calculate_salary(self) -> float:
        # Example logic for calculating salary
        return self.salary

    def mark_attendance(self, status: bool):
        self.attendance.append(status)

    def request_leave(self, leave: Leave):
        self.leaves.append(leave)
        leave.apply_leave()

    def evaluate_performance(self, performance: Performance):
        self.performance = performance
        performance.evaluate()

# class EmployeeManager:
#     def __init__(self):
#         data = np.genfromtxt('employee_data.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')
#
#         self.employees: List[Employee] = []
#
#     def add_employee(self, employee: Employee):
#
#         self.employees.append(employee)
#
#     def remove_employee(self, employee_id: int):
#         self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
#
#     def get_employee(self, employee_id: int) -> Employee:
#         for emp in self.employees:
#             if emp.employee_id == employee_id:
#                 return emp
#         return None
#
#     def list_employees(self) -> List[Employee]:
#         return self.employees
