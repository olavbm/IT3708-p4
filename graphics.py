import pygame
import time
from pygame import gfxdraw

windowDimensions = [700, 700]
grid = [10, 10]
cellSize = [windowDimensions[0]/grid[0], windowDimensions[1]/grid[1]]
windowSurface = pygame.display.set_mode((windowDimensions[0], windowDimensions[1]), 0, 32)
backDrop = pygame.Rect(0, 0, windowDimensions[0], windowDimensions[1])

colours = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "green": (0, 255, 0),
        "grey":  (100, 100, 100),
        "red":   (255, 0 , 0)
    }
offsetVec = {
        "U": [-25,-26],
        "L": [-23,-29],
        "R": [-25,-26],
        "D": [-25,-28]
    }

# Helper-function that collects individual sprites from a big spritesheet.
def calculateClauseSpritesFromSheet(filename):
    gnomeSheet = {
            }
    sheet = pygame.image.load("clause.png")

    sheet.set_clip(pygame.Rect(16, 8, 46, 57))
    upSprite = sheet.subsurface(sheet.get_clip())
    gnomeSheet["U"] = upSprite

    sheet.set_clip(pygame.Rect(76, 7, 46, 57))
    upSprite = sheet.subsurface(sheet.get_clip())
    gnomeSheet["R"] = upSprite

    sheet.set_clip(pygame.Rect(24, 132, 46, 57))
    upSprite = sheet.subsurface(sheet.get_clip())
    gnomeSheet["L"] = upSprite

    sheet.set_clip(pygame.Rect(144, 68, 46, 57))
    upSprite = sheet.subsurface(sheet.get_clip())
    gnomeSheet["D"] = upSprite

    return gnomeSheet

gnomeSheet = calculateClauseSpritesFromSheet("clause.png")

# Helper-function that calculates a position in pixels given a matrix-index and cell size.
def calculatePosFromIndex(matrixIndex, cellSize):
    return [matrixIndex[0] * cellSize[0] + cellSize[0]/2, matrixIndex[1] * cellSize[1] + cellSize[1]/2]

def drawGrid(surface, numGrid, cellSize):
    surface.fill((255, 255, 255))
    for x in range(numGrid[0]):
        pygame.draw.aaline(windowSurface, colours["black"], (cellSize[0] * x, 0), (cellSize[0] * x, 700))

    for y in range(numGrid[1]):
        pygame.draw.aaline(windowSurface, colours["black"], (0, cellSize[1] * y), (700, cellSize[1] * y))

# Draws a food-sprite in the given cell(ex. [1, 2]) on the given surface.
def drawFood(surface, matrixIndex, cellSize, r):
    pos = calculatePosFromIndex(matrixIndex, cellSize)
    pygame.gfxdraw.filled_circle(windowSurface, pos[0], pos[1], r, colours["green"])

    # Drawing nice anti-aliased circle around the circle.
    pygame.gfxdraw.aacircle(windowSurface, pos[0], pos[1], r, colours["black"])

# Draws a poison-sprite in the given cell(ex. [4, 2]) on the given surface.
def drawPoison(surface, matrixIndex, cellSize, r):
    pos = calculatePosFromIndex(matrixIndex, cellSize)
    points = [[pos[0], pos[1] - r], [pos[0] + r, pos[1]], [pos[0], pos[1] + r], [pos[0] - r, pos[1]]]
    pygame.gfxdraw.filled_polygon(windowSurface, points, colours["red"])

    # Drawing nice anti-aliased line around the polygon
    points = [[pos[0], pos[1] - r], [pos[0] + r, pos[1]], [pos[0], pos[1]+r], [pos[0]-r, pos[1]]]
    pygame.gfxdraw.aapolygon(windowSurface, points, colours["black"])

# Finds what sprite needs to be drawn, and calls the according function to draw it in place.
def drawRune(surface, rune, matrixIndex, cellSize):
    if rune == 0:
        return
    if rune == "P":
        drawPoison(surface, matrixIndex, cellSize, 20)
    elif rune == "F":
        drawFood(surface, matrixIndex, cellSize, 20)
    else:
        drawGnome(surface, matrixIndex, cellSize, rune)
    # Add other runes here when needed

# Draws entire board, including background, lines and other sprites.
def drawBoardFromMatrix(surface, m, grid, cellSize):
    drawGrid(surface, grid, cellSize)
    for x in range(len(m)):
        for y in range(len(m[x])):
            drawRune(surface, m[x][y], [x, y], cellSize)

# Draws a gnome, in a given direction and cell.
def drawGnome(surface, matrixIndex, cellSize, direction):
    pos = calculatePosFromIndex(matrixIndex, cellSize)
    surface.blit(gnomeSheet[direction], [a + b for a, b in zip(pos, offsetVec[direction])])
