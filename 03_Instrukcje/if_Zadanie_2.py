#obierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

user_number_1 = int(input('Podaj piersza liczbe calkowita: '))
user_number_2 = int(input('Podaj druga liczbe calkowita: '))
user_sum = user_number_1+user_number_2

if user_sum > 100:
    print(f'Suma liczb {user_number_1} + {user_number_2} wynosi {user_sum}.')
else:
    print(f'Koniec')