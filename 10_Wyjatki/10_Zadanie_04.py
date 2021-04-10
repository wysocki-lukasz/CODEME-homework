# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję, która
# przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

collected_errors = []

def ave(user_numbers):

    suma = 0
    for i in user_numbers:
        suma += i
    result = suma / len(user_numbers)
    return result

def eksport(source):
    with open('lista_bledow.txt', mode='w') as f:
        f.write(source)

try:
    user_numbers = input('Podaj kilka liczb po przecinku i zakoncz wciskajac Enter:')
    numbers = user_numbers.split(',')
    final_number = list(map(int, numbers))

    print(final_number)
    print(ave(final_number))

except ValueError as err:
    result = 0
    print('Podane znaki nie są liczbami')
    collected_errors.append(err)

    print(collected_errors)
    eksport_tekst = str(collected_errors)
    eksport(eksport_tekst)




