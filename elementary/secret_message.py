'''
Дан кусок текста.
Соберите все заглавные буквы в одно слово в том порядке
как они встречаются в куске текста.
Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.",
если мы соберем все заглавные буквы, то получим сообщение "HELLO".
'''

def find_message(text):
    return ''.join(a for a in text if a.isupper())

if __name__ == '__main__':
    find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    find_message("hello world!") == ""
