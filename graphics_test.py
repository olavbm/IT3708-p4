import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def test_simple_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        matrix[0][0] = "O"
        matrix[0][1] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(2)

    def test_simple_graphics_from_matrix(self):
        matrix = [ ["N" for i in range(30)] for i in range(15)]

        matrix[8][4] = "O"
        matrix[9][4] = "O"
        matrix[10][4] = "O"

        matrix[14][14] = "A"
        matrix[13][14] = "A"
        matrix[12][14] = "A"
        matrix[11][14] = "A"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
