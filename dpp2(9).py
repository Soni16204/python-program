#Write a Python program that takes a sentence as input and counts the number of words in it. A word is defined as a sequence of characters separated by spaces 
def count_words(sentence):
    words=sentence.split()
    return len(words)
sentence=input("enter the sentence:")
words_count=count_words(sentence)
print(f"the number of words in the sentence is:{words_count}")