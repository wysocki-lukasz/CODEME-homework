# coding=utf-8
# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

target = 5
previous_close = -50

def check_value(target, user_value, previous_close):
    if abs(target-user_value) < abs(previous_close):
        print("Cieplej")
        previous_close = abs(target-user_value)
    elif abs(target-user_value) >= abs(previous_close):
        print("Zimno")
    return previous_close

while True:
    user_value = int(input("Podaj twoja liczbe"))
    if user_value == target:

        break
    previous_close = check_value(target, user_value, previous_close)

print('Gratulacje, trafiles!')