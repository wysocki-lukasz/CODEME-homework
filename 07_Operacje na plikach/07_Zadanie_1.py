# coding=utf-8
# encoding = 'utf-8'
# 1▹ Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#           be or not to be?
# **************************************
#
# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
# plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

cytaty = ['Cytat 1', 'Cytat 2', 'Cytat 3', 'Cytat 4', 'Cytat 5', 'Cytat 6', 'Cytat 7', 'Cytat 8', 'Cytat 9', 'Cytat 10']

filename = 'cytat.txt'
with open(filename, 'w') as f:
  f.write('\n'.join(cytaty))

def cytat_generator(cytaty):
  import random
  selected_sentece = random.sample(cytaty, 1)
  return selected_sentece

def show(selected_sentece):
  print (60* '-')
  print (selected_sentece[0].center(60))
  print (60* '-')

show(cytat_generator(cytaty))


