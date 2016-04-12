import beer
import copy
import pprint
import random
import time
import unittest

class TestBeer(unittest.TestCase):
    def test_spawn_agent(self):
        board = [ ["N" for y in range(30)] for x in range(15)]
        board = beer.spawn_agent(board)

        counter = 0
        for x in board:
            for y in x:
                if y == "A":
                    counter += 1
        assert counter == 5
    def test_spawn_object(self):
        board = [ ["N" for y in range(30)] for x in range(15)]
        board = beer.spawn_object(board)

        counter = 0
        for x in board:
            for y in x:
                if y in "SB":
                    counter += 1
        assert 0 < counter < 7

    def test_fall(self):
        board = beer.create_board([30, 15])
        beer.fall(board)
        assert "S" in board[1] or "B" in board[1]












if __name__ == '__main__':
    unittest.main()
