#Write a Python function find_greater_than(lst, n) that accepts a list lst of numbers and a number n. The function should return a new list containing only the numbers greater than n.
def find_greater_than(lst,n):
    for num in lst:
        if(num>n):
            return num
numbers=[1,5,8,2,10,3]
result=find_greater_than(numbers,4)
print(result)