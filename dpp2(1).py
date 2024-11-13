#write a python program to check if a string is a pailndrome(read the same faword and backwords)
def ispalindrome(string):
    if(string==string[::-1]):
       return "the string is a palindrome"
    else:
        return "this is not palindrome"
string=input("enter string:")
print(ispalindrome(string))