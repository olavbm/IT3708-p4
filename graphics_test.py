import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def test_simple_graphics_from_matrix(self):
        matrix = [ [0 for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        for i in range(10):
            matrix[i][4] = "F"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)

    def testFoodPoisonClauseFromMatrix(self):
        matrix = [ [0 for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        for i in range(10):
            matrix[i][4] = "F"

        matrix[5][7] = "D"
        matrix[1][4] = "U"
        matrix[0][9] = "R"
        matrix[3][0] = "L"

        painter = graphics.Painter()
        painter.draw_board_from_matrix(matrix)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
