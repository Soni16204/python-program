#write a python program to reverse a string
input_string=input("enter a string to reverse:")
def reverse_string(s):
    return s[::-1]
reversed_string =reverse_string(input_string)
print("Reversed string:",reversed_string)