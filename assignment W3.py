# Define the Employee class with properties: companyId, departmentId, firstName, lastName, emailId, age, and salary.
class Employee:
    def __init__(self, companyId, departmentId, firstName, lastName, emailId, age, salary):
        # Initialize the properties of the Employee class.
        self.companyId = companyId
        self.departmentId = departmentId
        self.firstName = firstName
        self.lastName = lastName
        self.emailId = emailId
        self.age = age
        self.salary = salary

    # Define a method called calculateBonus (default implementation).
    def calculateBonus(self):
        # Default implementation for bonus calculation (can be overridden in subclasses).
        return 0

    def __str__(self):
        # Provide a formatted string representation of the employee.
        return f"Employee Details:\nCompany ID: {self.companyId}\nDepartment ID: {self.departmentId}\nName: {self.firstName} {self.lastName}\nEmail ID: {self.emailId}\nAge: {self.age}\nSalary: {self.salary}"


# Define a subclass called Manager, inheriting from the Employee class.
class Manager(Employee):
    def __init__(self, companyId, departmentId, firstName, lastName, emailId, age, salary, numSubordinates):
        # Call the __init__ method of the base class (Employee) using super() to initialize common properties.
        super().__init__(companyId, departmentId, firstName, lastName, emailId, age, salary)
        # Add a specific property for Manager: numSubordinates.
        self.numSubordinates = numSubordinates

    # Override the calculateBonus method to provide the bonus calculation specific to Managers.
    def calculateBonus(self):
        # Bonus calculation for Manager: 10% of the salary per subordinate.
        return 0.1 * self.salary * self.numSubordinates


# Define a subclass called Engineer, inheriting from the Employee class.
class Engineer(Employee):
    def __init__(self, companyId, departmentId, firstName, lastName, emailId, age, salary, numProjectsCompleted):
        # Call the __init__ method of the base class (Employee) using super() to initialize common properties.
        super().__init__(companyId, departmentId, firstName, lastName, emailId, age, salary)
        # Add a specific property for Engineer: numProjectsCompleted.
        self.numProjectsCompleted = numProjectsCompleted

    # Override the calculateBonus method to provide the bonus calculation specific to Engineers.
    def calculateBonus(self):
        # Bonus calculation for Engineer: 5% of the salary per project completed.
        return 0.05 * self.salary * self.numProjectsCompleted


# Create instances of the Manager and Engineer classes.
manager1 = Manager("C001", "D001", "John", "Doe", "john.doe@example.com", 35, 80000, 5)
engineer1 = Engineer("C001", "D001", "Jane", "Smith", "jane.smith@example.com", 28, 60000, 10)

# Print the employee details and bonuses.
print(manager1)
print("Manager 1 Bonus:", manager1.calculateBonus())

print(engineer1)
print("Engineer 1 Bonus:", engineer1.calculateBonus())