# coding=utf-8
#1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def bmi(wzrost, waga):
    bmi_value = waga/ (wzrost**2)

    if bmi_value >= 30:
        result = 'Nadwaga'
    elif 30 > bmi_value > 18.5:
        result = 'Waga normalna'
    elif bmi_value <= 18.5:
        result = 'Niedowaga'
    else:
        result = 'Blad w podaniu wartosci'
    return result


wzrost = int(input("Podaj wzrost w [m]:"))
waga = int(input("Podaj wage w [kg]:"))
print(bmi(wzrost,waga))