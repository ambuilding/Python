import random
import numpy as np

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

board = create_board()
#place(board, 1, (0, 0))

def possibilities(board):
    return list(zip(*np.where(board == 0)))

possibilities(board)

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

random_place(board, 2)

#for i in range(3):
#    random_place(board, 1)
#    random_place(board, 2)
#
#print(board)

def row_win(board, player):
    if np.any(np.all(board==player,axis=1)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False

#row_win(board, 1)
        
def col_win(board, player):
    if np.any(np.all(board==player,axis=0)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False
    
def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_game()

import matplotlib.pyplot as plt
import time
start = time.time()
games = [play_game() for i in range(1000)]
stop = time.time()
print(stop - start)
plt.hist(games)
plt.show()

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            random_place(board, player)
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            
            if winner != 0:
                break
    return winner

start = time.time()
games = [play_strategic_game() for i in range(1000)]
stop = time.time()
print(stop - start)
plt.hist(games)
plt.show()