# coding=utf-8
# 5▹ Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.
def reader(file):
    with open(file, 'r') as pt:
        content = pt.read()
    return content

def longest_word(text_update):
    longest = ''
    for word in text_update:
        if len(word) > len(longest):
            longest = word
    return longest

file = 'pan_tadeusz.txt'
text = reader(file)

text_update = text.replace('!', '').replace(',', '').replace('.', '').replace(';', '')

words_list = text_update.split()

print(words_list)
print(50*'-')
print(longest_word((words_list)))

