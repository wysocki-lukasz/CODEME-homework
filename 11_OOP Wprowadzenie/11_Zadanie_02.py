# 2▹ Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.

class Storczyk:
    def __init__(self, kolor, pora_kwitnienia, gatunek):
        self.kolor = kolor
        self.pora_kwitnienia = pora_kwitnienia
        self.gatunek = gatunek

    def wzrost(self):
        return "wysoko"

blady = Storczyk('blady', 'kwiecien', 'blady')
print(blady.kolor)