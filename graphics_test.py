import unittest
import graphics
import time
import pygame

class TestGraphics(unittest.TestCase):
    def testGraphicsFromMatrix(self):
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
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()
