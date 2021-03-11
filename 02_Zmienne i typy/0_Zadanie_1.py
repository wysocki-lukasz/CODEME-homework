#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

fuel_consumption = 6.4
distance = 120
price_per_litr = 5.04

travel_cost = round(float(distance/100 * fuel_consumption * price_per_litr),2)
print(f'Koszt zaplanowanej trasy wyniesie: {travel_cost} ZL')