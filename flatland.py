import random

pad = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
        }

# Values in the sense_pad is given in the order: F L R according to the given
# direction.
sense_pad = {
        "U": [pad["U"], pad["L"], pad["R"]],
        "R": [pad["R"], pad["U"], pad["D"]],
        "D": [pad["D"], pad["R"], pad["L"]],
        "L": [pad["L"], pad["D"], pad["U"]],
        }

board = [[]]
# Create a matrix holding a board of the given size.  Also fills the board with
# food and poison in accordance to Flatland.
def create_board(size, f, p):
    board = [[0 for i in range(size)] for i in range(size)]
    for x in range(len(board)):
        for y in range(len(board[x])):
            if random.random() < f:
                board[x][y] = "F"
            elif random.random() < p:
                board[x][y] = "P"

    return board

# For generating all boards being used on a ea-generation.
def init_boards(num_boards, size, f, p):
    boards = [[]]
    for i in range(num_boards):
        boards.append(create_board(size, f, p))

    return boards


# Get the position of the player from a board.
def get_pos(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] in pad:
                return [x, y]

# For manipulating the board according to an action given by the ann. Gives
# back anew board with the player moved, as well as the rune in the new square.
def modify_on_action(board, action):
    n = len(board)
    old_pos = get_pos(board)
    offset = pad[action]
    new_pos = ((old_pos[0] + offset[0]) % n, (old_pos[1] + offset[1]) % n)
    rune = board[new_pos[0]][new_pos[1]]

    board[new_pos[0]][new_pos[1]] = action
    board[old_pos[0]][old_pos[1]] = 0
    return board, rune

# Get the sensor-cells according to which position and direciton the player is
# looking.
def sensor_cells(board):
    n = len(board)
    pos = get_pos(board)
    direction = board[pos[0]][pos[1]]
    cells = sense_pad[direction]
    sensor_cells = []
    for cell in cells:
        sensor_cells.append(board
                [(pos[0] + cell[0]) % n]
                [(pos[1] + cell[1]) % n])
    return sensor_cells






































