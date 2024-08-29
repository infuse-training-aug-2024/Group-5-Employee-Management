from datetime import datetime
import os
import csv


class Leave:
    def apply_leave(self, employee_id, start_date, end_date, available_leaves):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.applied_date = datetime.today()
        self.available_leaves = available_leaves - 1
        status = 'waiting'
        leave_details = [employee_id, self.start_date, self.end_date, self.applied_date, self.available_leaves, status]
        self.write_to_csv('employee_leaves_data.csv', leave_details)

    def write_to_csv(self, filename, leave_details):
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Employee ID', 'Start Date', 'End Date', 'Applied on', 'Available leaves', 'status'])
            writer.writerow(leave_details)

    def show_leaves_left(self, employee_id, available_leaves):
        print("leaves left for employee id:", employee_id, " are =", available_leaves)

    def update_status(self, employee_id, new_status):
        self.employee_id = employee_id
        self.new_status = new_status
        rows = []
        latest_entry = None
        with open('employee_leaves_data.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:

                if row['id'] == str(self.employee_id):
                    applied_date = datetime.strptime(row['applied_date'], '%Y-%m-%d')
                    if not latest_entry or applied_date > datetime.strptime(latest_entry['applied_date'], '%Y-%m-%d'):
                        latest_entry = row

                rows.append(row)
        if latest_entry:
            print(f"Latest entry for Employee ID {self.employee_id}: {latest_entry}")

            # Update the 'available leaves' for the latest entry
            latest_entry['status'] = str(self.new_status)

            # Write the updated rows back to the CSV file
            with open('employee_leaves_data.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            print(f"Updated available leaves for Employee ID {employee_id} to {new_status}.")
        else:
            print(f"Employee ID {employee_id} not found in the file.")

    # Example usage

