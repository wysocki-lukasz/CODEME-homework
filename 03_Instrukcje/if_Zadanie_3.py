# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
# ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

counter = 3

scores = []

for opinia in range(counter):
    score = float(input(f"Prosze podac opinie w skali 0 - 10 ksiazki "))
    scores.append(score)

med_score = sum(scores)/len(scores)
print(f'Srednia ocen ksiazki to {med_score}')

if med_score > 7:
    print("Ocena ksiazki BARDZO DOBRA")
elif 5 <= med_score <= 7:
    print("Ocena ksiazki SREDNIA")
elif med_score < 5:
    print("Ocena ksiazki NIE WARTA UWAGI")