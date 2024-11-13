#Create a function is_positive(num) that checks if a given number is positive. The function should return True if the number is positive and False otherwise
def is_positive(num):
    if(num>0):
        return "true"
    else:
        return "false"
num=int(input("enter the number:"))
result=is_positive(num)
print(result)
    