# Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

items = ['ksiazka', 'termos', 'czpka', 'mapa', 'plecka', 'aparat']
print(items)
items_mod = sorted(items, key=str.lower)
print(items_mod)