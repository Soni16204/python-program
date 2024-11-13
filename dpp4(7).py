#Create a function count_vowels(s) that takes a string s as input and returns the number of vowels in the string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
str=input("enter the word:")
result = count_vowels(str)
print(result) 
