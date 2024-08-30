from performance import Performance
from employee_manager import EmployeeManager
from employee import Employee
#from leaves import Leave

def employee_specific_functions(input_employee_id):
    print("""
1) Accounts
2) Performance
3) Leaves  
        """)
    manager_choice_in_employee = int(input())

    match manager_choice_in_employee:
        # case 1:
        # # actions
        case 2:
            print("Give scores for the following employee criteria:")
            behaviour = int(input("Enter Behaviour Rating (1-5): "))
            team_collaboration = int(input("Enter Team Collaboration Rating (1-5): "))
            verbal_skills = int(input("Enter Verbal Skills Rating (1-5): "))
            critical_thinking = int(input("Enter Critical Thinking Rating (1-5): "))
            emotional_intelligence = int(input("Enter Emotional Intelligence Rating (1-5): "))
            per = Performance(input_employee_id, behaviour, team_collaboration, verbal_skills, critical_thinking, emotional_intelligence)
            per.save_to_csv()
        # actions


        case 3:

            print("""
            1) Apply for leave
            2) Update leave status
            3) Display available leaves
                """)

            print("leave functions: ")
            leave_variable = int(input("Enter your choice: "))
            l = Leave()
            match leave_variable:
                case 1:
                    emp = EmployeeManager()
                    remaining_leaves = emp.get_employee_leave(input_employee_id)
                    print(remaining_leaves)
                    # l.apply_leave()

            l = Leave()



            # actions
        # case _:
        # # default


def main():
    print("""
1) Add Employee
2) Display all Employee
3) Select employee using Id ()
4) Remove Employee 
    """)
    manager_choice = int(input())
    employeemanager = EmployeeManager()
    match manager_choice:
        case 1:
            employeemanager.add_employee()
        case 2:
            employeemanager.list_employees()
        case 3:
            input_employee_id = int(input("Enter employee_id: "))
            #check employee is valid
            employee_specific_functions(input_employee_id)
            #actions
        case 4:
            input_employee_id = int(input("Enter employee_id: "))
            employeemanager.remove_employee(input_employee_id)
        case _:
            print("Invalid option")

main()