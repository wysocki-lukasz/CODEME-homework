# coding=utf-8
# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def range(a,b, number):
    if number >= a and number <=b:
        result = 'Liczba znajduje sie w podanym przedziale'
    elif number >= b and number <= a:
        result = 'Liczba znajduje sie w podanym przedziale'
    else:
        result = 'Liczba jest poza zakresem'
    return result


print(range(7,9,4))
