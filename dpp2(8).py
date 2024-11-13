#Write a Python program to check if two strings are anagrams (contain the same characters in a different order).
def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
string1=input("enter the first string:")
string2=input("enter the second string:")
if are_anagrams(string1,string2):
    print("the string are anagrams")
else:
    print("the string are not anagrams")