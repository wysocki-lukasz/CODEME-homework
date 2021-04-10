# 5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ?
#Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

def calculate_BMI(mass, height):
    bmi = mass / (height ** 2)
    bmi_rounded = round(bmi, 2)

    if bmi_rounded < 18:
        return "underweight"
    elif 18 <= bmi_rounded < 25:
        return "normal"
    elif 25 <= bmi_rounded < 30:
        return "overweight"
    elif bmi_rounded >= 30:
        return "obesity"
    else:
        return "Something went wrong."

def get_weight():
    question = 'Podaj wage w kg: '
    weight = ask_user(question, 30, 250)
    return weight

def get_height():
    return ask_user('Podaj wzrost w metrach: ', 1.5, 2.35)

def ask_user(question, minimum, maximum):
    while True:
        try:
            value = float(input(question))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if minimum < value < maximum:
            break
        else:
            print('Podana wartość jest nieprawdopodobna. Spróbuj jeszcze raz')

    return value


if __name__ == "__main__":
    m = get_weight()
    h = get_height()
    result = calculate_BMI(m, h)
    print(result)
