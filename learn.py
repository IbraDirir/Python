#battleship game
board = []
for num in range(5):
    board.append(["O"] * 5)
#custom print
def print_board(board):
    for item in board:
        print(" ".join(item)) #print without  commas, or join the list
print_board(board)
#import function(randint)

from random import randint
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
random_row(board)
random_col(board)
