#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

ref_word = 'Palindrom'
user_word = input('Wprowadz wyrazenie: ')

user_word = user_word.lower().replace(' ','')


print(f'Czy podane wyrazenie jest palindromem? -> {user_word == user_word[::-1]}')