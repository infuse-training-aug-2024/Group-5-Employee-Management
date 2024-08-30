import numpy as np

class FileHandling:

    @classmethod
    def read_csv(cls , csv_file_name: str):

        try:
            data = np.genfromtxt(csv_file_name, delimiter=",", dtype=None, names=True, encoding='utf-8')
            return data

        except FileNotFoundError as fnf_error:
            print(f"Error: File '{csv_file_name}' not found. {fnf_error}")
            return None

        except ValueError as val_error:
            print(f"Error: Could not parse '{csv_file_name}' as CSV. {val_error}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
            return None


    @classmethod
    def save_info_employee(cls , employees: [], csv_file_name):
        try:
            data = []
            for employee in employees:
                data.append([
                    employee.employee_id,
                    employee.first_name,
                    employee.last_name,
                    employee.department,
                    employee.salary,
                    employee.designation,
                    employee.available_leaves,
                    employee.performance
                ])

            # Convert data to a NumPy array
            data_array = np.array(data, dtype=object)

            # Define the header
            header = ['employee_id', 'first_name', 'last_name', 'department', 'salary', 'designation',
                      'available_leaves',
                      'performance']

            # Save data to CSV file
            np.savetxt(csv_file_name, data_array, delimiter=',', header=','.join(header), comments='', fmt='%s')

        except FileNotFoundError as fnf_error:
            print(f"Error: File '{csv_file_name}' not found. {fnf_error}")
            return None

        except ValueError as val_error:
            print(f"Error: Could not parse '{csv_file_name}' as CSV. {val_error}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
            return None


