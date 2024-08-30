from datetime import datetime
import os
import csv
# from file_handling import read_csv
from file_handling import FileHandling
from employee_manager import EmployeeManager
leaves_data_filename='employee_leave_data.csv'
employee_data_filename='employee_data.csv'

class Leave:

    def take_leave(self, employee_id, start_date, end_date):
        

        try:
            available_leaves_str = EmployeeManager().get_employee_available_leaves(employee_id)
            applied_date = datetime.today()
            available_leaves = int(available_leaves_str) - 1
            leave_details = [employee_id, start_date, end_date,applied_date,available_leaves]
            FileHandling().save_leave_info(leave_details)
            
            
            EmployeeManager().set_employee_available_leaves(employee_id, available_leaves)


            
        except Exception as e:
            print(f"An error occurred while applying leave: {e}")

    

    def show_leaves_left(self, employee_id):
        try:
            employee_data=FileHandling.read_csv(employee_data_filename)
            for row in employee_data:
                if int(row['employee_id'])==employee_id:
                    employee_leaves=EmployeeManager.get_employee_available_leaves(employee_id)
                    print("Leaves left for employee id:", employee_id, " are =", employee_leaves)
        except Exception as e:
            print(f"An error occurred while showing leaves left: {e}")

    

leave_manager = Leave()
leave_manager.take_leave(124, '2024-09-01', '2024-09-05')
# leave_manager.show_leaves_left(106)
# print(EmployeeManager().get_employee_available_leaves(124))