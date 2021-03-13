### Kółko i krzyżyk:
#Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy.
#Wpisz w google "tic tac toe game" i zagraj z google.
#- Zacznij od zaprojektowania rozgrywki
#- Możliwość nazwania graczy inaczej niż X / O
#- Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
#    - Konieczność użycia modułu `random`.

board = [[1], [2], [3],
           [4], [5], [6],
           [7], [8], [9]]


# definiowanie planszy
def boards(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])


print('KÓŁKO I KRZYŻK - POWODZENIA!')
print('Uwaga: kazdy gracz wykonuje ruch poprzez wybarnie nr pola wpisujac cyfre od 1 do 9')
boards(board)

player_name = input('Podaj znak, który wybierasz: X - krzyzyk lub O - kolko (litera O): ').upper()
if player_name == 'X' or player_name == 'O':
    print('Powodzenia graczu {} !!!'.format(player_name))
else:
    print('Wpisany znak jest niewlasciwy, prosze prowadz litere X lub litere O')
    player_name = input('Podaj znak, który wybierasz: X - krzyzyk lub O - kolko (litera O): ').upper()

move_number = 0

for i in range(0, 10):
    print('Kolej {} . Gdzie postawic znak? Wybierz pole od 1 do 9'.format(player_name))
    player_move = int(input())
    actual_move = (player_move) - 1
    if board[actual_move] != 'X' and board[actual_move] != 'O':
        move_number += 1
        board[actual_move] = player_name
        boards(board)
    elif board[actual_move] == 'X' or board[actual_move] == 'O':
        print('To miejsce jest już zajęte, wybierz inne z zakresu 1 do 9')
    if player_name == 'X':
        player_name = 'O'
    else:
        player_name = 'X'

    if move_number >= 5 and move_number < 9:
        if board[0] == board[1] == board[2]:
            print("Wygrana", board[0])
            break
        elif board[3] == board[4] == board[5]:
            print("Wygrana", board[3])
            break
        elif board[6] == board[7] == board[8]:
            print("Wygrana", board[6])
            break
        elif board[0] == board[3] == board[6]:
            print("Wygrana", board[0])
            break
        elif board[1] == board[4] == board[7]:
            print("Wygrana", board[1])
            break
        elif board[2] == board[5] == board[8]:
            print("Wygrana", board[2])
            break
        elif board[0] == board[4] == board[8]:
            print("Wygrana", board[0])
            break
        elif board[2] == board[4] == board[6]:
            print("Wygrana", board[2])
            break
    if move_number == 9:
        print('Nikt nie wygrał. Koniec gry!')
        break

