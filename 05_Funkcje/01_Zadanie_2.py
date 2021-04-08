# coding=utf-8
# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def is_even_number(n):
    if n%2 ==0:
        a= "Liczba jest liczbą parzystą"

    else:
        a="Liczba nie jest liczbą parzystą"
    return a

print(is_even_number(5))

