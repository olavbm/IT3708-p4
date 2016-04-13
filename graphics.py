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

    def draw_rect(self, color, x, y, w):
        self.window_surface.fill(self.colours[color],
                [self.cell_size[0] * x, self.cell_size[1] * y, self.cell_size[0] * w, self.cell_size[1]])
        if (x + w) > self.grid[0]:
            self.draw_rect(color, 0, self.grid[1], (x + w) % self.grid[0])

    def draw_tracker(self, tracker_pos):
        self.draw_rect('blue', tracker_pos, self.grid[1], 5)

    def draw_object(self, object_pos, object_width, object_height):
        if object_width > 4:
            color = 'red'
        else:
            color = 'green'

        self.draw_rect(color, object_pos, self.grid[1] - object_height, object_width)


    # Draws entire board, including background, lines and other shapes
    def draw_board(self, things):
        self.draw_grid()
        self.draw_object(things['object_pos'], things['object_width'], things['object_height'])
        self.draw_tracker(things['tracker_pos'])
        pygame.display.update()
