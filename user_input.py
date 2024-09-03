import re


class UserInput:

    def get_employee_first_name(self):

        try:
            while True:
                first_name = input("Enter employee first name: ").strip()
                if re.match("^[A-Za-z]+$", first_name):
                    return first_name
                else:
                    print("First name must only contain letters and no spaces, numbers, or symbols. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_employee_last_name(self):

        try:
            while True:
                last_name = input("Enter employee last name: ").strip()
                if re.match("^[A-Za-z]+$", last_name):
                    return last_name
                else:
                    print("Last name must only contain letters and no spaces, numbers, or symbols. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_employee_department(self):
        while True:
            try:
                print("""Select Department for new Employee
    1) IT
    2) Accounts
                """)
                manager_choice = int(input("Enter: "))
                match manager_choice:
                    case 1:
                        return "it"
                    case 2:
                        return "accounts"
                    case _:
                        print("Select a valid option")
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_employee_salary(self):
        try:
            while True:
                salary = input("Enter employee salary amount: ").strip()

                # Check if salary is a valid positive number
                if salary.isdigit() and int(salary) > 0:
                    return int(salary)  # Return the salary as an integer
                else:
                    print("Salary must be a positive number. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


    def get_employee_designation(self):
        while True:
            try:
                print("""Select designation for new Employee
    1) tester
    2) software developer
                """)
                manager_choice = int(input("Enter: "))
                match manager_choice:
                    case 1:
                        return "tester"
                    case 2:
                        return "software developer"
                    case _:
                        print("Select a valid option")
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_employee_id(self) -> int:
        try:
            while True:
                employee_id = int(input("Enter employee ID: ").strip())

                if int(employee_id) > 100 :
                    return employee_id
                else:
                    print("Incorrect ID. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")



    def get_leave_dates(self) -> (str,str):
        start_date_str = ""
        try:
            while True:
                start_date_str = str(input("Enter leave start date: "))
                break
        except:
            print("Enter valid start date")

        try:
            while True:
                end_date_str = str(input(("Enter leave end date: ")))
                return start_date_str,end_date_str
        except:
            print("Enter valid end date")








