# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

krotka = ('jeden', 'dwa', 'trzy')
collected_errors = []
try:
    krotka[1] = 'dziesiec'
except TypeError as e:
    print('Krotka jest niemodyfikalna')
    collected_errors.append(e)
