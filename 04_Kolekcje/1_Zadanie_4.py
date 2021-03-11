# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

counter = int(input('Podaj przysta liczbe cyfr: '))

numbers = []
for number in range(counter):
    number = int(input('Podaj kolejna liczbe: '))
    numbers.append(number)

if numbers[int(counter/2-1)] == numbers[int(counter/2)]:
    print('Srodkowe dwie liczby są takie same')
else:
    print('Srodkowe dwie liczby NIE są takie same')

print(numbers[int(counter/2-1)], numbers[int(counter/2)])