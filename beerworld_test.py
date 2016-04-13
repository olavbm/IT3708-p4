import beerworld
import copy
import pprint
import random
import time
import unittest
import graphics

class TestBeer(unittest.TestCase):
    def test_spawn_agent(self):
        beer = beerworld.Beer()

        counter = 0
        for x in beer.board:
            for y in x:
                if y == "A":
                    counter += 1
        assert counter == 5
    def test_spawn_object(self):
        beer = beerworld.Beer()

        counter = 0
        for x in beer.board:
            for y in x:
                if y in "SB":
                    counter += 1
        assert 0 < counter < 7

    def test_fall(self):
        beer = beerworld.Beer()
        beer.fall()
        assert "S" in beer.board[1] or "B" in beer.board[1]

    def test_modify_on_action(self):
        beer = beerworld.Beer()
        beer.modify_on_action(-4)

        counter = 0
        for x in beer.board:
            for y in x:
                if y == "A":
                    counter += 1
        assert counter == 5

    def test_sensor_cells(self):
        beer = beerworld.Beer()
        cells = beer.sensor_cells()
        print
        if 1 in cells:
            for x in beer.board:
                print x
            print cells

    def test_graphics_from_beerworld(self):
        beer = beerworld.Beer()
        painter = graphics.Painter()
        painter.draw_board_from_matrix(beer.board)
        print "len board", len(beer.board)
        print "len board[0]", len(beer.board[0])
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
