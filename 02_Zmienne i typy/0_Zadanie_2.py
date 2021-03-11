#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika

fuel_consumption = float(input('Podaj szacowana wartosc spalania auta w [l/100km] :').replace(',','.'))
distance = float(input('Podaj dlugosc trasy w [km] :').replace(',','.'))
price_per_litr = float(input('Podaj cene paliwa w [Zl/litr] :').replace(',','.'))

travel_cost = round(float(distance/100 * fuel_consumption * price_per_litr),2)
print(f'Koszt zaplanowanej trasy wyniesie: {travel_cost} ZL')