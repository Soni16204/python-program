#Write a Python program to convert a string to uppercase and lowercase
input_string=input("enter a string:")
def convert_string(s):
    uppercase=s.upper()
    lowercase=s.lower()
    return uppercase,lowercase
upper,lower=convert_string(input_string)
print("uppercase:",upper)
print("lowercase:",lower)