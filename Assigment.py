employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def add_employee():
    try:
        emp_id = int(input("Enter the employee ID you want to add: "))
        if emp_id in employees:
            print("Employee ID already exists. Please try again.")
            return
        name = input("Employee Name: ")
        age = int(input("Employee Age: "))
        department = input("Employee Department: ")
        salary = float(input("Employee Salary: "))
        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }
        print(f"Employee {name} added successfully.")
    except:
        print(" Invalid input. Please try again.")

def view_employees():
    try:
        if not employees:
            print(" No employees found.")
            return
        print("\n Employee List:")
        for emp_id, details in employees.items():
            print(f"Employee ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
    except:
        print(" An error occurred while viewing employees.")

def search_employee():
    try:
        emp_id = int(input("Enter the employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f" Employee Found -> ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")
        else:
            print(" Employee not found.")
    except:
        print(" Invalid input. Please try again.")

def main_menu():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
        except:
            print(" Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print(" Exiting the system. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

print("Welcome to the Employee Management System")
main_menu()