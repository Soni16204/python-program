#Write a Python program to find the first occurrence of a substring in a given string.
def find_substring(string,substring):
    index=string.find(substring)
    return index
main_string=input("enter the main string:")
sub_string=input("enter the substring to find:")
result=find_substring(main_string.sub_string)
if result!=-1:
    print(f"the substring 'sub_string' first occur at index:{result}")
else:
    print(f"the substring'(sub_string)' is not found in main string")