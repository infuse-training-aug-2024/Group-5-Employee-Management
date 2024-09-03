from datetime import datetime
from file_handling import FileHandling
from employee_manager import EmployeeManager
leaves_data_filename='employee_leave_data.csv'
employee_data_filename='employee_data.csv'

class Leave:

    def take_leave(self, employee_id, start_date, end_date):
        try:
            available_leaves = int(EmployeeManager().get_employee_available_leaves(employee_id))
            applied_date = datetime.today()
            available_leaves = available_leaves - 1
            leave_details = [employee_id, start_date, end_date,applied_date,available_leaves]
            FileHandling().save_leave_info(leave_details)
            EmployeeManager().set_employee_available_leaves(employee_id, available_leaves)

        except Exception as e:
            print(f"An error occurred while applying leave: {e}")

    

    def show_leaves_left(self, employee_id):
        print(EmployeeManager().get_employee_available_leaves(employee_id))

