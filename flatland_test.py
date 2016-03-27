import unittest
import flatland
import pprint
import random
import copy

class TestFlatland(unittest.TestCase):
    def test_generate_single_board(self):
        board = flatland.create_board(10, 0.1,0.2)
        assert board is not None

    def test_generate_num_boards(self):
        boards = flatland.init_boards(3, 3, 0.1, 0.1)
        for board in boards:
            assert board is not None


    def test_get_pos(self):
        board = flatland.create_board(5,0.1,0.2)
        board[1][3] = "U"
        pos = flatland.get_pos(board)
        self.assertEqual(pos, [1,3])

    def test_modify_board(self):
        board = flatland.create_board(5, 0.4, 0.1)
        board[1][1] = "U"
        b = copy.deepcopy(board)
        board, rune = flatland.modify_on_action(board, "L")
        self.assertNotEqual(b, board)

    def test_modify_board_eat_rune(self):
        board = flatland.create_board(5,0.3,0.1)
        board[1][1] = "U"
        board[1][2] = "F"
        board, rune = flatland.modify_on_action(board, "R")
        self.assertEqual(rune, "F")

    def test_sensor_cells(self):
        board = flatland.create_board(5, 0.3,0.2)
        board[1][3] = "U"
        sensor_cells = flatland.sensor_cells(board)
        for cell in sensor_cells:
            assert cell is not None

if __name__ == '__main__':
    unittest.main()
