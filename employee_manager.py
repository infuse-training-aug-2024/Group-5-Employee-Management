import csv
from tabulate import tabulate
from employee_record import Employee
import numpy as np
from typing import List

class EmployeeManager:
    def __init__(self):
        data = np.genfromtxt('employee_data.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')
        self.employees: List[Employee] = []
        for row in data:
            employee = Employee(
                employee_id=int(row['employee_id']),
                first_name=row['first_name'],
                last_name=row['last_name'],
                department=row['department'],
                salary=float(row['salary']),
                designation=row['designation'],
                available_leaves=row['available_leaves'],
                performance=int(row['performance'])
            )
            self.employees.append(employee)

    def get_employee_leave(self, employee_id: int) -> Employee:
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp.available_leaves

        return None

    def save_info(self):
        # Prepare data for saving
        data = []
        for employee in self.employees:
            data.append([
                employee.employee_id,
                employee.first_name,
                employee.last_name,
                employee.department,
                employee.salary,
                employee.designation,
                employee.available_leaves,
                employee.performance
            ])

        # Convert data to a NumPy array
        data_array = np.array(data, dtype=object)

        # Define the header
        header = ['employee_id', 'first_name', 'last_name', 'department', 'salary', 'designation', 'available_leaves',
                  'performance']

        # Save data to CSV file
        np.savetxt('employee_data.csv', data_array, delimiter=',', header=','.join(header), comments='', fmt='%s')



    def add_employee(self):
        print(self.employees)
        new_employee_id = self.employees[-1].employee_id+1
        first_name = input("Enter First Name of Employee: ")
        last_name = input("Enter Last Name of Employee: ")
        department = input("Enter Department Name: ")
        salary = float(input("Enter Salary: "))
        designation = input("Enter Designation: ")
        available_leaves = 24
        performance = 0
        new_employee = Employee(new_employee_id,first_name,last_name,department,salary,designation,available_leaves,performance)
        self.employees.append(new_employee)
        self.save_info()

    def remove_employee(self, employee_id: int):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        self.save_info()

    def get_employee(self, employee_id: int) -> Employee:
        for emp in self.employees:
            if emp.employee_id == employee_id:
                print(f"""   
        employee_id = {emp.employee_id}
        first_name = {emp.first_name}
        last_name = {emp.last_name}
        department = {emp.department}
        designation  = {emp.designation}
        salary = {emp.salary}
        available_leaves: {emp.available_leaves}
        performance = {emp.performance}
""")
                return emp

        return None

    def list_employees(self) -> List[Employee]:
        data = [
            [
                employee.employee_id,
                employee.first_name,
                employee.last_name,
                employee.department,
                employee.designation,
                employee.salary,
                employee.available_leaves,
                employee.performance
            ]
            for employee in self.employees
        ]

        # Define the headers
        headers = ["employee_id", "first_name", "last_name", "department", "designation", "salary", "available_leaves",
                   "performance"]

        # Print the table
        print(tabulate(data, headers=headers, tablefmt='grid'))



