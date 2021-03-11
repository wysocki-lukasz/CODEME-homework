# Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:
#
# Policz wszystkie znaki w napisie
# Nie modyfikując zmiennej wyświetl słowo wisdom
# Wyświetl tylko pierwszą połowę tekstu
# Wyświetl tylko kropkę
# Wyświetl od połowy tylko co trzecią literę cytatu
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
# Wyświetl cały cytat odwrotnie
# Zamień wisdom na słowo friendship

quote = 'Honesty is the first chapter in the book of wisdom.'
print(quote)

print('\n')

print('Liczenie znakow')
print(f'Zmienna quote posiad {len(quote)} znakow.')

print('\n')

print('Wyswietlenie wisdom')
quote_mod = quote[-7:-1]
print(quote_mod)

print('\n')

print('Wyświetl tylko pierwszą połowę tekstu')
quote_mod2 = quote[:26]
print(quote_mod2)

print('\n')

print('Wyświetl tylko kropkę')
print(quote[-1])

print('\n')

print('Wyświetl od połowy tylko co trzecią literę cytatu')
print(quote[25::3])

print('\n')

print('Wyświetl ‘Hnsyi h is hpe ntebo fwso.’')
print(quote[0::2])

print('\n')

print('Wyświetl cały cytat odwrotnie')
print(quote[::-1])

print('\n')
print('Zamień wisdom na słowo friendship')
quote_mod3 = quote.replace('wisdom', 'friendship')
print(quote_mod3)

