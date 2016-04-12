import random

pad = {
        "R": ( 1,  0),
        "D": ( 0,  1),
        "L": (-1,  0),
        }


# Helper function to get the value of a position
def index_board(board, pos):
    l = len(board)
    return board[pos[0] % l][pos[1] % l]

# Get the position of the player from a board.
def get_pos(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if index_board(board, (x, y)) in pad:
                return [x, y]

# Creates the board, with randomly spawned object and agent.
def create_board(size):
    board = [["N" for i in range(size[0])] for i in range(size[1])]
    bottom = len(board)

    board = spawn_agent(board)
    board = spawn_object(board)

    return board

# Spawns an agent. The agent is always in the bottom row, only moving left or right.
def spawn_agent(board):
    start_pos = random.randint(0, len(board[0]))
    agent_pos = [(start_pos + x) % len(board[0])  for x in range(5)]

    for pos in agent_pos:
        board[len(board) - 1][pos] = "A"

    return board

# Spawns an object, with random size and starting-position.
# The object is considered Small(S) if it's size is less than 5, otherwise it is big.
def spawn_object(board):
    size = random.randint(1,6)
    object_type = "S"
    if size > 4:
        object_type = "B"

    start_pos = random.randint(0, len(board[0]))
    object_pos = [(start_pos + x) % len(board[0]) for x in range(size)]

    for pos in object_pos:
        board[0][pos] = object_type

    return board

def fall(board):
    for x in range(len(board) - 2):
        if "S" in board[x] or "B" in board[x]:
            board[x + 1] = [ c for c in board[x]]
            board[x] = ["N" for i in range(len(board[0]))]
            break
    return board

# For manipulating the board according to an action given by the ann. Gives
# back anew board with the player moved, as well as the rune in the new square.
def modify_on_action(board, action):
    n = len(board)
    old_pos = get_pos(board)

    action = rulf_to_ruld(action, index_board(board, old_pos))
    if not action:
        return (board, '0')

    offset = pad[action]
    new_pos = ((old_pos[0] + offset[0]) % n, (old_pos[1] + offset[1]) % n)
    rune = index_board(board, new_pos)

    board[new_pos[0]][new_pos[1]] = action
    board[old_pos[0]][old_pos[1]] = 0
    return board, rune

# Get the new sensors cells in accordance with shadows made by the objects above.
def sensor_cells(board):


    return sensor_cells
