#How can you create a class that inherits from another class?
#○ Provide an example of inheritance in Python
#In Python, you can create a class that inherits from another class by specifying the parent class in parentheses after the name of the child class. This enables the child class to inherit attributes and methods from the parent class, allowing you to build on existing functionality.

#Here's an example demonstrating inheritance in Python:

#python
#Copy code
# Parent class
class Animal:
    def speak(self):
        return "The animal makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "The dog barks"

# Creating an instance of the child class
my_dog = Dog()
print(my_dog.speak())  # Output: The dog barks
#Explanation
#The Dog class inherits from the Animal class, so it has access to the methods and attributes of Animal.
#In this example, Dog overrides the speak method of Animal with its own version, which returns "The dog barks".
#When my_dog.speak() is called, it executes the speak method defined in the Dog class.