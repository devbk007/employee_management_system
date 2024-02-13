# Employee Management System

## Code Setup
Run the command
```bash
git clone "https://github.com/devbk007/employee_management_system.git"
```

## Virtual Environment Setup
Run the following commands after navigating to the project directory
```bash
pipenv shell
pipenv install
```

## How to interact with application?
Run the following command
```bash
python app.py
```
#### Enter the choice number
1. Add Department
2. Remove Department
3. View Department List
4. Add Employee
5. Remove Employee
6. View Employee List

To exit, press any other key

## Directory Structure
1. app.py : Main python file with classes and objects.
2. company.json : JSON file where data is stored on exiting and loaded on startup

## Type checking
Run the command
```bash
mypy app.py
```