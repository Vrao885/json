import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employee_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        employees = data['employees']
        employee_objects = []
        for emp in employees:
            employee_objects.append(Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State']))
        return employee_objects

def print_employee_objects(employees):
    for emp in employees:
        print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")

if __name__ == "__main__":
    file_path = "employee.json"
    employees_list = read_employee_data_from_json(file_path)
    print_employee_objects(employees_list)
