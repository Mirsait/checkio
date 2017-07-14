import re

def is_get_three_words(text):
    words = re.findall('\D+\s\D+\s\D+',text, re.IGNORECASE)
    return len(words)>0

if __name__ == '__main__':
    is_get_three_words("Hello World hello") == True
    is_get_three_words("He is 123 man") == False
    is_get_three_words("1 2 3 4") == False
    is_get_three_words("bla bla bla bla") == True
    is_get_three_words("Hi") == False
    is_get_three_words("one two 3 four five six 7 eight 9 ten eleven 12") == True
