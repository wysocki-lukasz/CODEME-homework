# 1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
# atrybuty: imię, kolor sierści, rasę
# metody: szczekaj, machaj ogonem

class Pies:
    def __init__(self, imie, kolor_siersci, rasa):
        self.imie = imie
        self.kolor_siersci = kolor_siersci
        self.rasa = rasa

    def szczekanie(self):
        return 'hau'

    def machaj_ogonem(self):
        return self.imie + 'machanie'

figa = Pies('figa', 'czarny', 'kundelek')
print(figa.imie)

print(figa.machaj_ogonem())