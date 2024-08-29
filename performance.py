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
        self.average = (self.behaviour + self.critical_thinking + self.emotional_intelligence + self.team_collaboration + self.verbal_skills) / 5

    def save_to_csv(self, file_path='employee_performance_data.csv'):
        self.get_performance_avg()

        # Read the existing data
        updated = False
        rows = []

        if os.path.exists(file_path):
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row['employee_id']) == self.employee_id:
                        row['behaviour'] = self.behaviour
                        row['team_collaboration'] = self.team_collaboration
                        row['verbal_skills'] = self.verbal_skills
                        row['critical_thinking'] = self.critical_thinking
                        row['emotional_intelligence'] = self.emotional_intelligence
                        row['average'] = self.average
                        updated = True
                    rows.append(row)

        # If the employee_id wasn't found, append a new record
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

    def initialize(self):
        employee_id = int(input("Enter Employee ID: "))
        with open(emp_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['employee_id']) == employee_id:
                    behaviour = int(input("Enter Behaviour Rating (1-5): "))
                    team_collaboration = int(input("Enter Team Collaboration Rating (1-5): "))
                    verbal_skills = int(input("Enter Verbal Skills Rating (1-5): "))
                    critical_thinking = int(input("Enter Critical Thinking Rating (1-5): "))
                    emotional_intelligence = int(input("Enter Emotional Intelligence Rating (1-5): "))

                    employee = Performance(employee_id, behaviour, team_collaboration, verbal_skills, critical_thinking,
                                           emotional_intelligence)
                    employee.save_to_csv()
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                print("Employee id doesn't exist")