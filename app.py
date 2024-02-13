from typing import List, Dict
import json

class Employee:
    """Details of an employee such as name, id and department name
    """
    def __init__(self, name:str, id:int, department:str = None) -> None:
        self._name = name
        self._id = id
        self._department = department
    
    def employee_details(self)->None:
        """Print name, id and department of employee
        """
        print(f"Name : {self._name}, ID : {self._id}, Department : {self._department}")

    def __str__(self) -> str:
        """
        Returns:
            str: Employee name, id and department
        """
        return f"Name : {self._name}, ID : {self._id}, Department : {self._department}"

class Department:
    """Details of a department such as department name and list of employees within the department
    """
    def __init__(self, dept_name:str) -> None:
        self._dept_name = dept_name
        self._employees: List[Employee] = []

    def add_employee(self, *args) -> None:
        """Add an employee to the department
        Can give single employee object or multiple employee objects as arguments
        """
        for employee in args:
            employee._department = self._dept_name # Update the department name
            self._employees.append(employee)
        print("Employee added")
    
    def remove_employee(self, emp_id:int) -> bool:
        """Removes an employee from department

        Args:
            emp_id (int): Employee id

        Returns:
            bool: True, if employee present in the department is removed. False if the employee is not present in department 
        """
        if not self._employees:
            return False
        for employee in self._employees:
            if employee._id == emp_id:
                self._employees.remove(employee)
                print(f"Employee with id {emp_id} removed")
                return True
            
        return False
    
    def employee_list(self) -> None:
        """Prints details of employees in each department
        """
        if not self._employees:
            print(f"No employees in the {self._dept_name} department")
            return
        print(f"Employees in the {self._dept_name} department")
        for employee in self._employees:
            print(employee)

class Company:
    """Details of company such as departments and employees in each department
    """
    def __init__(self) -> None:
        self._departments:dict = {}

    def add_department(self, dept_name:str) -> None:
        """Add department if department does not exist

        Args:
            dept_name (str): Name of department
        """
        if dept_name not in self._departments:
            self._departments[dept_name] = Department(dept_name)
        else:
            print("Department already exists")
    
    def remove_department(self, dept_name:str) -> None:
        """Removes a department if it exists

        Args:
            dept_name (str): Name of department
        """
        if dept_name in self._departments:
            self._departments.pop(dept_name)
        else:
            print("Department does not exist")
    
    def department_list(self) -> None:
        """Prints names of departments if present
        """
        if not self._departments:
            print("Departments are empty")
            return
        print("Departments are : ", *self._departments.keys())


def menu() ->None:
    """
    List of choices for user to select
    """
    print("""
          Employee Management System
          
          Select Choice
            1- Add Department
            2- Remove Department
            3- View Department List
            4- Add Employee
            5- Remove Employee
            6- View Employee List
            Press any other key to exit
          """)

def load_department_data() -> Dict:

    """Loads department data from JSON file to the dictionary data structure of Company

    Returns:
        Dict: Dictionary with Department names as keys and Department objects as values
    """    
    try:
        with open("company.json", "r") as f:
            departments_data = json.load(f)
            departments = {}
            for dept_name, dept_data in departments_data.items():
                department = Department(dept_name)
                for emp_data in dept_data['employees']:
                    employee = Employee(emp_data['name'], emp_data['id'], dept_name)
                    department._employees.append(employee)
                departments[dept_name] = department
            return departments
    except FileNotFoundError: # Create empty company.json file if file does not exist
        with open('company.json', 'w') as f:
            json.dump({},f)
        return {}

    except Exception as e:
        print(e)
        return {} # Return empty dictionary

def save_data(department: Dict) ->None:
    """Save department data to JSON file

    Args:
        department (str): Department name
    """
    with open("company.json", "w") as f:
        json.dump(department, f, default=lambda x: x.__dict__)


if __name__ == "__main__":
    company = Company()
    company._departments = load_department_data()
    while True:
        menu()
        choice = input("Enter your choice : ")
        if choice == "1":
            company.add_department(input("Enter department name : "))
        elif choice == "2":
            company.remove_department(input("Enter department name : "))
        elif choice == "3":
            company.department_list()
        elif choice == "4":
            emp_name = input("Enter employee name : ")
            id = int(input("Enter employee id : "))
            dept_name = input("Enter department : ")
            if dept_name in company._departments:
                emp = Employee(emp_name, id, dept_name)
                company._departments[dept_name].add_employee(emp)
            else:
                print("Department does not exist")
        elif choice == "5":
            removed = False
            emp_id = int(input("Enter employee id : "))
            for dept_name, department in company._departments.items():
                if department.remove_employee(emp_id):
                    removed = True

            if not removed:
                print(f"Employee with id {emp_id} does not exist")
        elif choice == "6":
            if not company._departments:
                print("Empty departments")
            else:
                for dept_name, department in company._departments.items():
                    department.employee_list()
        else:
            print("Exiting...")
            save_data(company._departments)
            break

