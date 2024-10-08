from tabulate import tabulate
from employee import Employee
from typing import List
from file_handling import FileHandling
from user_input import UserInput

class EmployeeManager:

    def __init__(self):

        data = FileHandling.read_csv("employee_data.csv")
        self.employees: List[Employee] = []
        for row in data:
            employee = Employee(int(row['employee_id']),row['first_name'],row['last_name'],row['department'],float(row['salary']),row['designation'],row['available_leaves'],int(row['performance'])
            )
            self.employees.append(employee)



    def add_employee(self):
        userinput = UserInput()
        new_employee_id = self.employees[-1].employee_id + 1
        input_first_name = userinput.get_employee_first_name()
        input_last_name = userinput.get_employee_last_name()
        input_department = userinput.get_employee_department()
        input_salary = userinput.get_employee_salary()
        input_designation = userinput.get_employee_designation()
        available_leaves = 24
        performance = 0
        new_employee = Employee(new_employee_id,input_first_name,input_last_name,input_department,input_salary,input_designation,available_leaves,performance)
        self.employees.append(new_employee)
        FileHandling.save_info_employee(self.employees,"employee_data.csv")

    def remove_employee(self, employee_id: int):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        FileHandling.save_info_employee(self.employees,"employee_data.csv")

    def get_employee(self, employee_id: int) -> Employee|None:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def print_employee(self, employee_id: int) :
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print(f"""employee_id = {employee.employee_id}
first_name = {employee.first_name}
last_name = {employee.last_name}
department = {employee.department}
designation  = {employee.designation}
salary = {employee.salary}
available_leaves: {employee.available_leaves}
performance = {employee.performance}
""")


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
        headers = ["employee_id", "first_name", "last_name", "department", "designation", "salary", "available_leaves",
                   "performance"]

        print(tabulate(data, headers=headers, tablefmt='grid'))

    def get_employee_salary(self, employee_id: int) -> float | None:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee.salary
        return None

    def get_employee_performance(self, employee_id: int) -> int|None:
        for employee in self.employees :
            if employee.employee_id == employee_id:
                return employee.performance
        return None

    def get_employee_available_leaves(self, employee_id: int) -> int|None:
        for employee in self.employees:
            if employee.employee_id == employee_id:

                return employee.available_leaves
        return None

    def set_employee_performance(self, employee_id: int , average_performance: int):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.performance = average_performance
        FileHandling.save_info_employee(self.employees,"employee_data.csv")
        return None

    def set_employee_available_leaves(self, employee_id: int , updated_available_leaves: int):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.available_leaves = updated_available_leaves
        FileHandling.save_info_employee(self.employees,"employee_data.csv")
        return None

    def is_valid_employee_id(self, employee_id: int)->bool:
        for employee in self.employees:
            if employee_id == employee.employee_id:
                return True
        return False

