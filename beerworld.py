import random

class Beer(object):
    def __init__(self):
        self.size = [30, 15]
        self.board = []
        self.object_height = -1
        self.agent_pos = []
        self.object_pos = []
        self.pad = {
            "R": ( 1,  0),
            "D": ( 0,  1),
            "L": (-1,  0),
            }
        self.create_board()

    # Helper function to get the value of a position
    def index_board(self, pos):
        l = len(self.board)
        return self.board[pos[0] % l][pos[1] % l]

    # Get the position of the player from a board.
    def get_pos(self):
        for x in range(len(self.board)):
            for y in range(len(board[x])):
                if index_board(board, (x, y)) in pad:
                    return [x, y]

    # Creates the board, with randomly spawned object and agent.
    def create_board(self):
        self.board = [["N" for i in range(self.size[0])] for i in range(self.size[1])]
        self.spawn_agent()
        self.spawn_object()


    # Spawns an agent. The agent is always in the bottom row, only moving left or right.
    def spawn_agent(self):
        start_pos = random.randint(0, len(self.board[0]))
        agent_pos = [(start_pos + x) % len(self.board[0])  for x in range(5)]
        self.agent_pos = agent_pos

        for pos in agent_pos:
            self.board[len(self.board) - 1][pos] = "A"

    # Spawns an object, with random size and starting-position.
    # The object is considered Small(S) if it's size is less than 5, otherwise it is big.
    def spawn_object(self):
        object_height = len(self.board)
        self.object_height = object_height
        size = random.randint(1,6)
        object_type = "S"
        if size > 4:
            object_type = "B"

        start_pos = random.randint(0, len(self.board[0]))
        object_pos = [(start_pos + x) % len(self.board[0]) for x in range(size)]
        self.object_pos = object_pos

        for pos in object_pos:
            self.board[0][pos] = object_type

    # The object falls down 1 row each timestep
    def fall(self):
        for x in range(len(self.board) - 2):
            if "S" in self.board[x] or "B" in self.board[x]:
                self.board[x + 1] = [ c for c in self.board[x]]
                self.board[x] = ["N" for i in range(len(self.board[0]))]
                break
        self.object_height -= 1

    # TODO: Might want to optimize and rewrite this code
    # For manipulating the board according to an action given by the ann. Gives
    # back anew board with the player moved, as well as the reaction(e.
    def modify_on_action(self, action):
        bottom = len(self.board) - 1

        start_index = action
        self.agent_pos = [(self.agent_pos[i] + action) % 30 for i in range(len(self.agent_pos))]

        intersection = filter(lambda x: x in self.agent_pos, self.object_pos)
        reaction = "N"
        if self.object_height == 0 and len(intersection) != 0:
            if len(self.object_pos) > 4:
                reaction = "B"
            elif len(intersection) == len(self.object_pos) and len(self.object_pos) < 5:
                reaction = "S"

        for x in range(len(self.board[bottom])):
            if self.board[bottom][x] == "A":
                start_index = (start_index + x) % len(self.board[bottom])
                break

        bottom_list = ["N" for i in range(len(self.board[bottom]))]
        for x in range(len(self.board[bottom])):
            for i in range(5):
                bottom_list[(start_index + i) % len(self.board[bottom])] = "A"

        self.board[bottom] = bottom_list

        if self.object_height == 0:
            self.spawn_object()
        else:
            self.fall()
        return self.board, reaction

    # Get the new sensors cells in accordance with shadows made by the objects above.
    def sensor_cells(self):
        cells = [0 for i in range(len(self.agent_pos))]
        for i in range(len(self.agent_pos)):
            if self.agent_pos[i] in self.object_pos:
                cells[i] = 1
        return cells
