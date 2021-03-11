#Dokładnie 75 godziny. Tyle czasu wg. naukowców potrzeba, aby nabyć nową umiejętność.
#Oblicz ile pełnych tygodni zajmie Ci zdobycie nowej umiejętności,
# w zależności o tego, ile czasu jesteś wstanie poświęcić na naukę w tygodniu.

hours_for_learnig = 75
hours_avaliable = int(input('Podaj liczbe calkowita godzin w tygodniu do nauki:' ))

weeks_for_learnig = round(hours_for_learnig / hours_avaliable)
print(f'Wymagana czas do nabycia nowej umiejestnosci to {weeks_for_learnig} tygodni!')