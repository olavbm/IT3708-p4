import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def test_single_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        matrix[0][0] = "S"
        matrix[0][1] = "A"

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

        matrix[8][4] = "B"
        matrix[9][4] = "B"
        matrix[10][4] = "B"
        matrix[11][4] = "B"
        matrix[12][4] = "B"
        matrix[12][4] = "B"

        matrix[14][14] = "A"
        matrix[13][14] = "A"
        matrix[12][14] = "A"
        matrix[11][14] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
