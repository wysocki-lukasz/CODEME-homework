def wisieles(chance, password):

    tablica = list(password)
    for i in range(len(password)):
        tablica[i] = '_'

    chance = 6

    while chance > 0:
        print('Pozostalo Tobie', chance, 'zycia.')
        print(' '.join(tablica))

        letter = str(input("Podaj swoja litere:")).lower()

        if letter in password:
            for i in range(len(password)):
                if password[i] == letter:
                    tablica[i] = letter

            if str(tablica) == str(password):
                print('Wygrales!')
                break
        else:
            chance -= 1
    return tablica