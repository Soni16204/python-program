#What are magic methods in Python?
#○ Define magic methods and provide examples of commonly used ones (e.g.,
#__str__, __repr__).
#Magic methods (also known as dunder methods, short for "double underscore") in Python are special methods with double underscores at the beginning and end of their names, like __init__, __str__, and __repr__. These methods are predefined by Python and allow objects of a class to implement and customize behaviors for built-in operations and functions. Magic methods provide a way to define how objects of a class should respond to operations like addition, comparisons, string representations, and more.

#__str__: Defines the informal (or user-friendly) string representation of an object, which is shown when using print() or str() on the object. This is meant to be readable and human-friendly.

#python
#Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old
#__repr__: Defines the official (or developer-friendly) string representation of an object, often used in debugging. This representation is more formal and intended to be unambiguous.

#python
#Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
#Generally, __str__ is meant for end-users, while __repr__ is for developers.