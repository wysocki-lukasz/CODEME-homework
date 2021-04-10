print("Modul BMI zaimportowany")

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
