# 3▹ Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

element = [13, 'string', 2.45, 0, 'jeden', [], 3, 'osiem', 2222, ()]
collected_errors = []

try:
    index_user = input('Podaj index: ')
    result = 1 / element[index_user]
except TypeError as e:
    result = 0
    print("Blad typu: TypeError")
    print("Probojesz wykonac dzielenie 1 /")
    collected_errors.append(e)
except ZeroDivisionError as e:
    result = 1
    print("Blad dzielenia przez 0: ZeroDivisionError")
    print("Probojesz wykonac dzielenie 1 /"+ element[index_user])
    collected_errors.append(e)

print(result)

