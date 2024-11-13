#What is the __init__ method?
#○ Explain the purpose of the __init__ method in a class.
#The __init__ method in Python is a special method called a constructor. Its main purpose is to initialize an object’s attributes when it is created. 
# The __init__ method is automatically called when a new instance of a class is created, allowing you to set up the initial state of the object.

#Key Points of __init__:
#Initialization of Attributes: The __init__ method lets you define attributes and set them to specific values when an object is created, 
# making sure that each instance of a class starts with its required properties.

#Automatic Execution: When you create a new object by calling the class name (e.g., my_object = MyClass()), Python automatically calls the __init__ method on that object.

#Self Parameter: The first parameter of __init__ is always self, which refers to the instance being created. 
# This parameter is required so that __init__ can assign values to the instance’s attributes.

#Optional Arguments: You can also pass additional arguments to __init__ to initialize attributes with specific values, making the object flexible and reusable.