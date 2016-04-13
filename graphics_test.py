import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def test_single_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        matrix[8][0] = "S"
        matrix[8][9] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)

    def test_small_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(30)] for i in range(15)]

        matrix[8][4] = "S"
        matrix[9][4] = "S"
        matrix[10][4] = "S"

        matrix[14][14] = "A"
        matrix[13][14] = "A"
        matrix[12][14] = "A"
        matrix[11][14] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)
    def test_big_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(30)] for i in range(15)]

        matrix[8][4] = "S"
        matrix[9][4] = "S"
        matrix[10][4] = "S"

        matrix[14][14] = "A"
        matrix[13][14] = "A"
        matrix[12][14] = "A"
        matrix[11][14] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)
    def test_simple_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(30)] for i in range(15)]
        print len(matrix)

        matrix[0][0] = "B"
        matrix[1][0] = "B"
        matrix[2][0] = "B"
        matrix[3][0] = "B"
        matrix[4][0] = "B"
        matrix[5][0] = "B"

        matrix[14][14] = "A"
        matrix[13][14] = "A"
        matrix[12][14] = "A"
        matrix[11][14] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
