# Employee class to represent an employee
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_employee(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


# Company class to manage the employees
class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []  # List to hold employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employe(self):
        if not self.employees:
            print("No employees in the company.")
        else:
            print(f"Employees of {self.company_name}:")
            for emp in self.employees:
                print(emp.display_employee())

    def total_salary(self):
        total = sum(emp.salary for emp in self.employees)
        return total

    def search_employee_by_id(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp.display_employee()
        return "Employee not found."

    def remove_employee_by_id(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                self.employees.remove(emp)
                return f"Employee with ID {employee_id} has been removed."
        return "Employee not found."


# Example Usage of the Classes

# Create a company
company = Company("TechCorp")

# Create employee objects
employee1 = Employee(1, "Akshat", "Business manager", 300000)
employee2 = Employee(2, "Jenish", "Data Scientist", 1.500000)
employee3 = Employee(3, "Prince", "HR Manager", 1.300000)

# Add employees to the company
company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

# Display all employees
company.display_all_employe()

# Calculate total salary of all employees
print(f"Total salary of all employees: ${company.total_salary()}")

# Search for an employee by ID
print(company.search_employee_by_id(1))  # Search by ID 2 (Bob)

# Remove an employee by ID
print(company.remove_employee_by_id(3))  # Remove employee with ID 3 (Charlie)

# Display all employees after removal
company.display_all_employe()

