import pygame
import time

windowDimensions = [700, 700]
grid = [10, 10]
cellSize = [windowDimensions[0]/grid[0], windowDimensions[1]/grid[1]]
windowSurface = pygame.display.set_mode((windowDimensions[0], windowDimensions[1]), 0, 32)
windowSurface.fill((255, 255, 255))

colours = {
    "black": (0, 0, 0),
    "green": (0, 255, 0)
    }

def drawGrid(numGrid, cellSize):
    for x in range(numGrid[0]):
        pygame.draw.aaline(windowSurface, colours["black"], (cellSize[0] * x, 0), (cellSize[0] * x, 700))

    for y in range(numGrid[1]):
        pygame.draw.aaline(windowSurface, colours["black"], (0, cellSize[1] * y), (700, cellSize[1] * y))


drawGrid(grid, cellSize)

pygame.display.update()
time.sleep(1)
