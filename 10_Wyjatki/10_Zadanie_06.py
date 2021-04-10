# 6▹ Wywołaj błąd związany z otwarciem pliku.
#
# Spróbuj odczytać plik, który nie istnieje.
# Spróbuj odczytać wartość z pliku otwartym w trybie w
# Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.

try:
    with open('plik.txt') as f:
        print(f.readline())
except FileNotFoundError as err:
    print('Podane plik nie istnieje')

try:
    with open('plik.txt', mode = 'w') as f:
        print(f.readline())
except io.UnsupportedOperation as err:
    print('Podane plik nie istnieje')

try:
    with open('lista_bledow.txt', mode='x') as f:
        f.write('Piekna pogoda')
except FileExistsError as err:
    print('Podany plik juz istnieje')