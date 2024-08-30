import csv
import os

emp_file_path = 'employee_data.csv'


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
        self.average = (self.behaviour + self.critical_thinking + self.emotional_intelligence +
                        self.team_collaboration + self.verbal_skills) / 5

    def save_to_csv(self):
        file_path='employee_performance_data.csv'
        self.get_performance_avg()

        updated = False
        rows = []

        try:
            if os.path.exists(file_path):
                with open(file_path, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            if int(row['employee_id']) == self.employee_id:
                                row['behaviour'] = self.behaviour
                                row['team_collaboration'] = self.team_collaboration
                                row['verbal_skills'] = self.verbal_skills
                                row['critical_thinking'] = self.critical_thinking
                                row['emotional_intelligence'] = self.emotional_intelligence
                                row['average'] = self.average
                                updated = True
                        except ValueError:
                            print(f"Skipping invalid row with employee_id: {row['employee_id']}")
                        rows.append(row)

            if not updated:
                rows.append({
                    'employee_id': self.employee_id,
                    'behaviour': self.behaviour,
                    'team_collaboration': self.team_collaboration,
                    'verbal_skills': self.verbal_skills,
                    'critical_thinking': self.critical_thinking,
                    'emotional_intelligence': self.emotional_intelligence,
                    'average': self.average
                })

            with open(file_path, mode='w', newline='') as file:
                fieldnames = ['employee_id', 'behaviour', 'team_collaboration', 'verbal_skills', 'critical_thinking',
                              'emotional_intelligence', 'average']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(rows)

            print(f"Performance data for employee_id {self.employee_id} saved successfully.")

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied when accessing the file '{file_path}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

