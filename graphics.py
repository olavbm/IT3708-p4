import pygame
from pygame import gfxdraw

class Painter:
    def __init__(self):
        self.window_dimensions = [700, 700]
        self.grid = [10, 10]
        self.cell_size = [self.window_dimensions[0]/self.grid[0], self.window_dimensions[1]/self.grid[1]]
        self.window_surface = pygame.display.set_mode((self.window_dimensions[0], self.window_dimensions[1]), 0, 32)
        self.gnome_sheet = self.calculate_claus_sprites_from_sheet("clause.png")
        self.colours = {
                "black": (0, 0, 0),
                "white": (255, 255, 255),
                "green": (0, 255, 0),
                "grey":  (100, 100, 100),
                "red":   (255, 0 , 0)
            }
        self.offset_vec = {
                "U": [-25,-26],
                "L": [-23,-29],
                "R": [-25,-26],
                "D": [-25,-28]
            }

    # Helper-function that collects individual sprites from a big spritesheet.
    def calculate_claus_sprites_from_sheet(self, filename):
        gnome_sheet = {}
        sheet = pygame.image.load("clause.png")

        sheet.set_clip(pygame.Rect(16, 8, 46, 57))
        gnome_sheet["U"] = sheet.subsurface(sheet.get_clip())

        sheet.set_clip(pygame.Rect(76, 7, 46, 57))
        gnome_sheet["R"] = sheet.subsurface(sheet.get_clip())

        sheet.set_clip(pygame.Rect(24, 132, 46, 57))
        gnome_sheet["L"] = sheet.subsurface(sheet.get_clip())

        sheet.set_clip(pygame.Rect(144, 68, 46, 57))
        gnome_sheet["D"] = sheet.subsurface(sheet.get_clip())

        return gnome_sheet

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

    # Draws a food-sprite in the given cell(ex. [1, 2]) on our surface.
    def draw_food(self, matrix_index, r):
        pos = self.calculate_pos_from_index(matrix_index)
        pygame.gfxdraw.filled_circle(self.window_surface, pos[0], pos[1], r, self.colours["green"])

        # Drawing nice anti-aliased circle around the circle.
        pygame.gfxdraw.aacircle(self.window_surface, pos[0], pos[1], r, self.colours["black"])

    # Draws a poison-sprite in the given cell(ex. [4, 2]) on the given surface.
    def draw_poison(self, matrix_index, r):
        pos = self.calculate_pos_from_index(matrix_index)
        points = [[pos[0], pos[1] - r], [pos[0] + r, pos[1]], [pos[0], pos[1] + r], [pos[0] - r, pos[1]]]
        pygame.gfxdraw.filled_polygon(self.window_surface, points, self.colours["red"])

        # Drawing nice anti-aliased line around the polygon
        points = [[pos[0], pos[1] - r], [pos[0] + r, pos[1]], [pos[0], pos[1] + r], [pos[0] - r, pos[1]]]
        pygame.gfxdraw.aapolygon(self.window_surface, points, self.colours["black"])

    # Draws a gnome, in a given direction and cell.
    def draw_gnome(self, matrix_index, direction):
        pos = self.calculate_pos_from_index(matrix_index)
        self.window_surface.blit(self.gnome_sheet[direction], [a + b for a, b in zip(pos, self.offset_vec[direction])])

    # Finds what sprite needs to be drawn, and calls the according function to draw it in place.
    def draw_rune(self, rune, matrix_index):
        if rune == 0:
            return
        elif rune == "F":
            self.draw_food(matrix_index, 20)
        elif rune == "P":
            self.draw_poison(matrix_index, 20)
        else:
            self.draw_gnome(matrix_index, rune)
        # Add other runes here when needed

    # Draws entire board, including background, lines and other sprites.
    def draw_board_from_matrix(self, matrix):
        self.draw_grid()
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                self.draw_rune(matrix[x][y], [x, y])
        pygame.display.update()
