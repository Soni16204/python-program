#Write a Python program to count the number of vowels in a given string
string= str(input("enter the value"))
vowels= "aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
print("number of vowels:",count)