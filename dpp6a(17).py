#What is the difference between a class method and a static method?
#○ Compare class methods and static methods with code examples
#The main difference between a class method and a static method in Python is their relationship with the class and instances:

#Class Method:

#Defined using the @classmethod decorator.
#Takes cls as the first parameter, representing the class itself.
#Can access or modify class variables and call other class methods.
#Often used for factory methods or methods that work with class-level data.
#Static Method:

#Defined using the @staticmethod decorator.
#Does not take self or cls as a parameter.
#Operates independently of class or instance data—essentially like a regular function that is namespaced within the class.
#Useful for utility functions related to the class but not dependent on instance or class data.
#Here’s a side-by-side comparison with examples:

#Class Method Example
#In this example, we’ll use a class method to create a new instance from a formatted string.

#python
#Copy code
class Employee:
    # Class attribute to track employee count
    employee_count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1  # Update count for each new instance

    # Class method to return the employee count
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Class method to create an Employee instance from a string
    @classmethod
    def from_string(cls, employee_str):
        name, position = employee_str.split("-")
        return cls(name, position)

# Creating instances using the constructor and class method
emp1 = Employee("Alice", "Developer")
emp2 = Employee.from_string("Bob-Manager")

# Accessing the class method
print(Employee.get_employee_count())  # Output: 2
#In this case, get_employee_count and from_string are class methods. get_employee_count accesses the class attribute, while from_string provides an alternative way to create an Employee instance from a string.

#Static Method Example
#Now, we’ll add a static method that performs a utility function, such as validating a department name. It doesn’t interact with class-level or instance-level data.

#python
#Copy code
class Employee:
    # Class attribute to track employee count
    employee_count = 0
    valid_departments = ["HR", "Engineering", "Marketing", "Finance"]

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1

    # Class method to get employee count
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Static method to validate department names
    @staticmethod
    def is_valid_department(department):
        return department in Employee.valid_departments

# Using the static method to validate a department
print(Employee.is_valid_department("Engineering"))  # Output: True
print(Employee.is_valid_department("Legal"))        # Output: False
