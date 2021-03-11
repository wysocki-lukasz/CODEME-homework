# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numbers = []
for number in range(4):
    number = int(input('Podaj kolejna liczbe: '))
    numbers.append(number)

print(f'Liczby wpisane przez uzytkownika to: {numbers} ')

if numbers[0] == numbers[-1]:
    print('Wpisana liczba pierwsza i ostatnia są takie same')
else:
    print('Wpisane liczby pierwsza i ostatnia nie sa takie same')