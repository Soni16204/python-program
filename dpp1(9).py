#count the number of vowels in a string using a for loop
string= str(input("enter the value"))
vowels= "aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
print("number of vowels:",count)