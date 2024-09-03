import csv
from employee_manager import EmployeeManager
from file_handling import FileHandling
import numpy as np

class Performance:
    def __init__(self, employee_id: int, behaviour: int, team_collaboration: int, verbal_skills: int,
                 critical_thinking: int, emotional_intelligence: int):
        self.employee_id = employee_id
        self.behaviour = behaviour
        self.team_collaboration = team_collaboration
        self.verbal_skills = verbal_skills
        self.critical_thinking = critical_thinking
        self.emotional_intelligence = emotional_intelligence
        self.average = 0

    def get_performance_avg(self):
        self.average = (self.behaviour + self.critical_thinking + self.emotional_intelligence + self.team_collaboration + self.verbal_skills) / 5

    def save_to_csv(self, file_path='employee_performance_data.csv'):
        self.get_performance_avg()

        updated = False
        rows = []

    # Use the FileHandling class to read the CSV file as a numpy structured array
        data = FileHandling.read_csv(file_path)

        if data is not None:
            # Check if the data is a 0-d array and handle it accordingly
            if data.ndim == 0:
                # Single entry case
                if data['employee_id'] == self.employee_id:
                    data['behaviour'] = self.behaviour
                    data['team_collaboration'] = self.team_collaboration
                    data['verbal_skills'] = self.verbal_skills
                    data['critical_thinking'] = self.critical_thinking
                    data['emotional_intelligence'] = self.emotional_intelligence
                    data['average'] = self.average
                    updated = True
                rows.append(data)  # Ensure it's added as a tuple
            else:
                # Normal case, iterate over each row
                for row in data:
                    if row['employee_id'] == self.employee_id:
                        row['behaviour'] = self.behaviour
                        row['team_collaboration'] = self.team_collaboration
                        row['verbal_skills'] = self.verbal_skills
                        row['critical_thinking'] = self.critical_thinking
                        row['emotional_intelligence'] = self.emotional_intelligence
                        row['average'] = self.average
                        updated = True
                    rows.append(tuple(row))  # Ensure each row is added as a tuple

        # If the employee_id wasn't found, append a new record
        if not updated:
            rows.append((
                self.employee_id, self.behaviour, self.team_collaboration, self.verbal_skills,
                self.critical_thinking, self.emotional_intelligence, self.average
            ))

        # Convert the rows list to a numpy structured array
        dtype = [('employee_id', 'i4'), ('behaviour', 'i4'), ('team_collaboration', 'i4'), ('verbal_skills', 'i4'),
                 ('critical_thinking', 'i4'), ('emotional_intelligence', 'i4'), ('average', 'f4')]
        rows_array = np.array(rows, dtype=dtype)

        # Save the numpy structured array back to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(rows_array.dtype.names)
            # Write data
            writer.writerows(rows_array)
    
        employee = EmployeeManager()
        employee.set_employee_performance(self.employee_id, self.average)
        print(f"Performance data for employee_id {self.employee_id} saved successfully.")
