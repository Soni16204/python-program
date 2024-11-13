#How can you create a property in a class?
#○ Explain how to use the property decorator to create a property and provide an
#example
#In Python, you can create a property in a class using the @property decorator. A property allows you to define methods that behave like attributes, enabling you to control access to instance variables and apply logic for getting, setting, and deleting attribute values. This is useful when you want to validate or modify data before accessing or changing it, without altering the attribute syntax.

#Using the @property Decorator
#To create a property with the @property decorator:

#Define a method with the @property decorator. This method will act as the getter for the property.
#To define a setter (optional), create another method with the same name and apply the @property_name.setter decorator.
#To define a deleter (optional), use @property_name.deleter.
#Example: Creating a Property
#Let’s create a class Rectangle with properties for width and height that calculate the area dynamically. We’ll use the @property decorator to control access to width and height, applying validation to ensure they are non-negative.

#python
#Copy code
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define the getter for width
    @property
    def width(self):
        return self._width

    # Define the setter for width with validation
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be non-negative")
        self._width = value

    # Define the getter for height
    @property
    def height(self):
        return self._height

    # Define the setter for height with validation
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

    # Property for area that depends on width and height
    @property
    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(5, 10)
print(rect.area)  # Output: 50

rect.width = 7
print(rect.area)  # Output: 70

# Trying to set a negative width raises a ValueError
# rect.width = -3  # Uncommenting this line will raise ValueError: Width must be non-negati