#Write a Python program that takes a string as input and returns a new string where each word's first letter is capitalized (also known as "title case"). For example, the input "hello world" should return "Hello World". Consider edge cases like multiple spaces between words.
def capitalize_words(sentence):
    words=sentence.split()
    capitalized_words=[word.capitalize() for word in words]
    return "".join(capitalized_words)
input_string=input("enter a string:")
result=capitalize_words(input_string)
print(f"capitalized string:{result}")
