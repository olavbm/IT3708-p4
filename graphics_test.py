import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def testSimpleGraphicsFromMatrix(self):
        matrix = [ [0 for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        for i in range(10):
            matrix[i][4] = "F"

        windowDimensions = [700, 700]
        grid = [10, 10]
        cellSize = [windowDimensions[0]/grid[0], windowDimensions[1]/grid[1]]
        windowSurface = pygame.display.set_mode((windowDimensions[0], windowDimensions[1]), 0, 32)

        pygame.display.update()
        graphics.drawBoardFromMatrix(windowSurface, matrix, grid, cellSize)
        pygame.display.update()
        time.sleep(1)

    def testFoodPoisonClauseFromMatrix(self):
        matrix = [ [0 for i in range(10)] for i in range(10)]
        matrix[3] = ["P" for i in range(10)]

        for i in range(10):
            matrix[i][4] = "F"

        windowDimensions = [700, 700]
        grid = [10, 10]
        cellSize = [windowDimensions[0]/grid[0], windowDimensions[1]/grid[1]]
        windowSurface = pygame.display.set_mode((windowDimensions[0], windowDimensions[1]), 0, 32)

        matrix[5][7] = "D"
        matrix[1][4] = "U"
        matrix[0][9] = "R"
        matrix[3][0] = "L"

        graphics.drawBoardFromMatrix(windowSurface, matrix, grid, cellSize)
        pygame.display.update()
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()
