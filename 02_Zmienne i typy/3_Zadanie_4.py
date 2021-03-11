# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

book_name = input('Podaj tytul ksiazki: ').capitalize()
book_author = input('Podaj autora ksiazki: ').capitalize()
book_pages = input('Podaj ilosc stron: ')

print(f'Sprawdzenie czy nazwa ksiazki sklada sie z liter: {book_name.isalpha()}.')
print(f'Sprawdzenie czy imie autora sklada sie z liter: {book_author.isalpha()}.')
print(f'Sprawdzenie czy liczba stron jest cyfra: {book_pages.isnumeric()}.')

book = book_name+' '+book_author+' '+book_pages
print(book)

print(f'Liczba wszystkich znakow w napise book to: {len(book)} znakow')

