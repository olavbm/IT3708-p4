import pygame
from pygame import gfxdraw

class Painter:
    def __init__(self):
        self.window_dimensions = [700, 700]
        self.grid = [30, 15]
        self.cell_size = [self.window_dimensions[0]/self.grid[0], self.window_dimensions[1]/self.grid[1]]
        self.window_surface = pygame.display.set_mode((self.window_dimensions[0], self.window_dimensions[1]), 0, 32)
        self.colours = {
                "black": (0, 0, 0),
                "white": (255, 255, 255),
                "green": (0, 255, 0),
                "grey":  (100, 100, 100),
                "red":   (255, 0 , 0),
                "blue":   (0, 0 , 255)
            }
        self.offset_vec = {
                "U": [-25,-26],
                "L": [-23,-29],
                "R": [-25,-26],
                "D": [-25,-28]
            }

    # Helper-function that calculates a position in pixels given a matrix-index and cell size.
    def calculate_pos_from_index(self, matrix_index):
        return [matrix_index[0] * self.cell_size[0] + self.cell_size[0]/2,
                matrix_index[1] * self.cell_size[1] + self.cell_size[1]/2]

    # Draws the entire grid, with background-color.
    def draw_grid(self):
        self.window_surface.fill((self.colours["white"]))
        for x in range(self.grid[0]):
            pygame.draw.aaline(self.window_surface, self.colours["black"], (self.cell_size[0] * x, 0), (self.cell_size[0] * x, 700))

        for y in range(self.grid[1]):
            pygame.draw.aaline(self.window_surface, self.colours["black"], (0, self.cell_size[1] * y), (700, self.cell_size[1] * y))

    # Draws a falling object in cell on surface. Does not handle the whole obejct, just a single square.
    # A small object is less than 5 squares in size
    def draw_small_object(self, matrix_index):
        pos = self.calculate_pos_from_index(matrix_index)
        self.window_surface.fill(self.colours["green"], [pos[0] - self.cell_size[0]/2, pos[1] - self.cell_size[1]/2, self.cell_size[0], self.cell_size[1]])

    # Draws a falling object in cell on surface. Does not handle the whole obejct, just a single square.
    def draw_big_object(self, matrix_index):
        pos = self.calculate_pos_from_index(matrix_index)
        self.window_surface.fill(self.colours["red"], [pos[0] - self.cell_size[0]/2, pos[1] - self.cell_size[1]/2, self.cell_size[0], self.cell_size[1]])

    # Draws an agent on the surface. Does not handle the whole agent, just a single square.
    def draw_agent(self, matrix_index):
        pos = self.calculate_pos_from_index(matrix_index)
        self.window_surface.fill(self.colours["blue"], [pos[0] - self.cell_size[0]/2, pos[1] - self.cell_size[1]/2, self.cell_size[0], self.cell_size[1]])

    # Finds what sprite needs to be drawn, and calls the according function to draw it in place.
    def draw_rune(self, rune, matrix_index):
        if rune == "N":
            return
        elif rune == "B":
            self.draw_big_object(matrix_index)
        elif rune == "S":
            self.draw_small_object(matrix_index)
        elif rune == "A":
            self.draw_agent(matrix_index)
        # Add other runes here when needed

    # Draws entire board, including background, lines and other shapes
    def draw_board_from_matrix(self, matrix):
        self.draw_grid()
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                self.draw_rune(matrix[x][y], [x, y])
        pygame.display.update()
