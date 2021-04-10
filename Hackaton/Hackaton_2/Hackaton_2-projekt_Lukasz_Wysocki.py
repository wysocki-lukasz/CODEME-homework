import json

# Wprowadzanego kontaktu
def contact_input(lista_numerow):

    while str(input('Czy chcesz wprowadzic kolejny kontakt? T/N ')).upper() == 'T':
        name_user_temp = str(input('Podaj imie wlasiciela numeru telefonu: '))
        phone_number_user_temp = input('Podaj numer telefonu komorkowy, 9 cyfr (+48) : ')
        name_user = str.lower(name_user_temp).capitalize()
        try:
            phone_number_user = int(phone_number_user_temp)
            wpis = {'imie': name_user, 'numer (+48)': phone_number_user}
            lista_numerow.append(wpis)
        except ValueError:
            print('Podany numer jest nieprawidlowy, posiada litery')

    else:
        print('Dziekuje za dodanie kontaktow')
    return lista_numerow

# Eksport pliku json
def eksport(source):
    with open('ksiazka_numerow.json', mode='w') as plik:
        json.dump(source, plik)

#Wczytanie pliku json

def import_json():
    filename= 'ksiazka_numerow.json'
    try:
        with open(filename, mode='r') as plik:
            lista_numerow = json.load(plik)
            print(f'Wczytano {len(lista_numerow)} wpisów.')
            return lista_numerow
    except FileNotFoundError:
        return []

#Wlasciwy kod
lista_numerow = []
current_lista_numerow = import_json()

if __name__ == '__main__':
   lista_numerow = contact_input(current_lista_numerow)

print(lista_numerow)

eksport(lista_numerow)

