from performance import Performance
from employee_manager import EmployeeManager
<<<<<<< HEAD
from leaves import Leave
from user_input import UserInput
from accounts import Payroll
=======
from employee import Employee
leaves import Leave

>>>>>>> f4c328bab15617bb179b9bebcdab40cdf1d620d3

def employee_specific_functions(input_employee_id):
    print("""
1) Accounts
2) Performance
3) Leaves  
        """)
    manager_choice_in_employee = int(input())

    match manager_choice_in_employee:
        case 1:
            payroll = Payroll(input_employee_id)
            print("""
1) Calculate total salary
2) Generate total salary bill           
            """)
            account_user_input = int(input("Select option: "))
            match account_user_input:
                case 1:
                    Payroll.calculate_total(payroll)
                case 2:
                    Payroll.generate_salary_slip(payroll)
                case _:
                    print("Invalid option")
        case 2:
            print("Give scores for the following employee criteria:")
            behaviour = int(input("Enter Behaviour Rating (1-5): "))
            team_collaboration = int(input("Enter Team Collaboration Rating (1-5): "))
            verbal_skills = int(input("Enter Verbal Skills Rating (1-5): "))
            critical_thinking = int(input("Enter Critical Thinking Rating (1-5): "))
            emotional_intelligence = int(input("Enter Emotional Intelligence Rating (1-5): "))
            per = Performance(input_employee_id, behaviour, team_collaboration, verbal_skills, critical_thinking, emotional_intelligence)
            per.save_to_csv()

        case 3:

            leave = Leave()
            print("""1) Apply for leave
2) Display available leaves
                """)
            leaves_user_input = int(input("Select option: "))
            match leaves_user_input:
                case 1:
                    start_date,end_date = UserInput().get_leave_dates()
                    leave.take_leave(input_employee_id,start_date, end_date)
                case 2:
                    leave.show_leaves_left(input_employee_id)
                case _:
                    print("Invalid option")

        case _:
            print("Invalid option")


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
            employee_id = UserInput().get_employee_id()
            if employeemanager.is_valid_employee_id(employee_id):
                employee_specific_functions(employee_id)
            else:
                print("Employee doest exist in database")
        case 4:
            input_employee_id = int(input("Enter employee_id: "))
            employeemanager.remove_employee(input_employee_id)
        case _:
            print("Invalid option")

main()