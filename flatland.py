import random

# Create a matrix holding a board of the given size.  Also fills the board with
# food and poison in accordance to Flatland.
def createBoard(size, f, p):
    board = [[0 for i in range(10)] for i in range(10)]

    # First we place the food.
    for x in range(len(board)):
        for y in range(len(board[x])):
            if random.random() < f:
                board[x][y] = "F"

    # First we place the poison.
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0 and random.random() < p:
                board[x][y] = "P"

    return board
