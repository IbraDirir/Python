#battleship game
board = []
for num in range(5):
    board.append(["O"] * 5)
#custom print
def print_board(board):
    for item in board:
        print(item)
print_board(board)