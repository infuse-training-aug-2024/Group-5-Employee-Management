from datetime import datetime
import os
import csv
# from file_handling import read_csv
from file_handling import FileHandling
leaves_data_filename='employee_leaves_data.csv'
employee_data_filename='employee_data.csv'

class Leave:

    def take_leave(self, employee_id, start_date, end_date, available_leaves):
        try:
            employee_data=FileHandling.read_csv(employee_data_filename)
            print(employee_data)
            leaves_data=FileHandling.read_csv(leaves_data_filename)
            for row in leaves_data:

                pass
            for row in employee_data:
                if int(row['employee_id'])==employee_id:
                    available_leaves = available_leaves - 1
                    FileHandling.save_info_employee()

            
        except Exception as e:
            print(f"An error occurred while applying leave: {e}")

    

    def show_leaves_left(self, employee_id, available_leaves):
        try:
            employee_data=FileHandling.read_csv(employee_data_filename)
            for row in employee_data:
                if int(row['employee_id'])==employee_id:
                    print("Leaves left for employee id:", employee_id, " are =", available_leaves)
        except Exception as e:
            print(f"An error occurred while showing leaves left: {e}")

    

leave_manager = Leave()
leave_manager.apply_leave(101, '2024-09-01', '2024-09-05', 5)
leave_manager.show_leaves_left()