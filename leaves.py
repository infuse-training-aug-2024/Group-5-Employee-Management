from datetime import date
import os
import csv

class Leave:
    def apply_leave(self, employee_id, start_date, end_date, available_leaves):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.applied_date = date.today()
        self.available_leaves= available_leaves-1
        leave_details = [employee_id, self.start_date, self.end_date,self.applied_date,self.available_leaves]
        self.write_to_csv('employee_leaves_data.csv', leave_details)
        
    def write_to_csv(self, filename, leave_details):
        file_exists = os.path.isfile(filename)
        
        with open(filename, mode='a') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['Employee ID', 'Start Date', 'End Date','Applied on', 'Available leaves'])
            
            writer.writerow(leave_details)

    

    def show_leaves_left(self,available_leaves):
          print("leaves left for employee id:",self.employee_id," are =",available_leaves)
        

employee_leave=Leave()
employee_leave.apply_leave(104,'2000-09-02','2000-09-02',6)
