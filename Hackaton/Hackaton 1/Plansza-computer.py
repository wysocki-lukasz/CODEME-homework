import random as r

board = [1,2,3,4,5,6,7,8,9]
for i in range(100):
    computer_move = r.randint(1, 9)
    if computer_move in board:
        board.remove(computer_move)
        print(computer_move)
        print(board)
    else:
        continue
