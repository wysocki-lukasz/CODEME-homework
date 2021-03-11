#Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków
# oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

user_word = str(input("Wpisz dowolny ciag znakow "))
len_user_word = len(user_word)
print(f'Dlugosc wprowadzonego ciagu znakow to {len_user_word} liter.')
print(f'Litera a pojawia sie {user_word.count("a")} razy')

if len_user_word > 5 and user_word.count("a")>0:
    user_word_mod = user_word.replace("a", "z")
    print("Dlugosc ciagu znakow > 5 oraz ciag znakow zawiera litere a")
    print(user_word_mod)
else:
    print("Dlugosc ciagu znakow < 5 oraz ciag znakow nie zawiera litere a")
    print(user_word)

