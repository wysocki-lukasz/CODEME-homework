# Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana
# przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”

user_number = int(input('Podaj liczbe calkowita: '))

if user_number % 3 == 0:
    print(f'Podama liczna {user_number} jest podzielna przez liczbe 3')
else:
    print(f'Podama liczna {user_number} NIE jest podzielna przez liczbe 3')