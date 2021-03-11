#Stwórz skrypt weeks.py. Napisz program, który obliczy i wyświetli liczbę minut w ciągu siedmiu tygodni.

minutes_per_hour = 60
hour_per_day = 24
day_per_week = 7
week_numbers = 7

hour_per_week = minutes_per_hour * hour_per_day * day_per_week
hour_per_7week = hour_per_week * week_numbers
print(f'Liczba minut w ciagu siedmiu tygodni = {hour_per_7week}. ')