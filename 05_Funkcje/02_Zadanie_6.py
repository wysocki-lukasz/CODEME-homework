# coding=utf-8
# 6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

def competition(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return ('Remis')
    elif player_1_choice == 1:
        if player_2_choice == 3 or player_2 == 2:
            return ('Wygrywa %s ! Gratulacje.' % player_1)
    elif player_1_choice == 2:
        if player_2_choice == 3:
            return ('Wygrywa %s ! Gratulacje.' % player_1)
        else:
            return ('Wygrywa %s ! Gratulacje.' % player_2)
    elif player_1_choice == 3:
        return ('Wygrywa %s ! Gratulacje.' % player_2)
    else:
        return ('to nie jest prawidlowy wybor')


#player_1 = str(input('Podaj imie gracza 1: '))
player_1 = 'Gracz 1'
player_2 = 'Gracz 2'
#player_2 = str(input('Podaj imie gracza 2: '))
print("--------------------------------- ")
print("Mozliwosc wyboru: ")
print("Wcisnij '1' - wybierasz Kamien ")
print("Wcisnij '2' - wybierasz Papier ")
print("Wcisnij '3' - wybierasz Nozyczki ")
print("---------------------------------- ")

player_1_choice = int(input(' %s: Wcisnij: 1-Kamien lub 2-Papier lub 3-Nozyczki: ' % player_1))
player_2_choice = int(input(' %s: Wcisnij: 1-Kamien lub 2-Papier lub 3-Nozyczki: ' % player_2))

print(competition(player_1_choice, player_2_choice))
