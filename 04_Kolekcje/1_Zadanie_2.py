#Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

numbers = []
for number in range(10):
    number = int(input('Podaj kolejna liczbe: '))
    numbers.append(number)

print(f'Liczby wpisane przez uzytkownika to: {numbers} ')

numbers_mod = []
for number in range(len(numbers)):
    if numbers[number] %2 == 0:
        numbers_mod.append(numbers[number])

print(f'Wpisane liczby parzyste to: {numbers_mod} ')
