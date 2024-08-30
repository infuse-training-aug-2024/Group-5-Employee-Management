from tabulate import tabulate
from employee_record import Employee
from typing import List
from file_handling import FileHandling

class EmployeeManager:



    def __init__(self):

        data = FileHandling().read_csv("employee_data.csv")
        self.employees: List[Employee] = []
        for row in data:
            employee = Employee(int(row['employee_id']),row['first_name'],row['last_name'],row['department'],float(row['salary']),row['designation'],row['available_leaves'],int(row['performance'])
            )
            self.employees.append(employee)




    def get_employee_leave(self, employee_id: int) -> int | None:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee.available_leaves
        return None




    def add_employee(self):

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
        FileHandling().save_info_employee(self.employees,"employee_data.csv")




    def remove_employee(self, employee_id: int):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        FileHandling().save_info_employee(self.employees,"employee_data.csv")




    def get_employee(self, employee_id: int) -> Employee|None:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print(f"""   
        employee_id = {employee.employee_id}
        first_name = {employee.first_name}
        last_name = {employee.last_name}
        department = {employee.department}
        designation  = {employee.designation}
        salary = {employee.salary}
        available_leaves: {employee.available_leaves}
        performance = {employee.performance}
""")
                return employee

        return None



    def list_employees(self):
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


    def set_employee_performance(self, employee_id: int , average_performance: float):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.performance = average_performance
        return None

