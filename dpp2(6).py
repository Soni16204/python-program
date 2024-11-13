#Write a Python program to replace all occurrences of a word in a string with another word.
def replace_word(string,old_word,new_word):
    return string.replace(old_word,new_word)
print(replace_word("hello world","world","everyone"))