#How can you override a method in a subclass?
#○ Write an example showing method overriding in inheritance
#In object-oriented programming, method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name, parameters, and return type as a method in the superclass, it "overrides" the superclass method. This is useful for customizing or extending the functionality of inherited methods.

#How to Override a Method in Python
#To override a method in Python:

#Define a method in the subclass with the same name as the method in the superclass.
#Provide a new implementation for the method in the subclass.
#You can also call the overridden method from the superclass within the subclass using super(). This is helpful if you want to retain some behavior from the superclass method and extend or modify it.

#Example of Method Overriding in Python
#Here’s an example that demonstrates method overriding in inheritance:

#python
#Copy code
# Superclass
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Subclass overriding the speak method
class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Subclass overriding the speak method
class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Example usage
animal = Animal()
animal.speak()  # Output: The animal makes a sound

dog = Dog()
dog.speak()     # Output: The dog barks

cat = Cat()
cat.speak()     # Output: The cat meows
#Calling the Superclass Method with super()
#If you want to use the superclass’s implementation within an overridden method, you can use super():

#python
#Copy code
class Bird(Animal):
    def speak(self):
        super().speak()  # Calls the superclass method
        print("The bird chirps")

# Example usage
bird = Bird()
bird.speak()
# Output:
# The animal makes a sound
# The bird chirps
#In this modified example, Bird calls super().speak() to first execute the speak method of Animal before adding its own behavior ("The bird chirps"). This is useful for extending rather than completely replacing the superclass’s behavior.