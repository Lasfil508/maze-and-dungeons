import pygame
from settings import *


class Map:
    def __init__(self, grid_cells):
        self.grid_cells = grid_cells.copy()
        self.obj = []
        self.mobs = []

    def render(self):
        for cell in self.grid_cells:
            x, y = cell.x * tile, cell.y * tile
            #pygame.draw.rect(cell.sc, pygame.Color('darkgrey'), (x, y, tile, tile), 1)

            if cell.walls['top']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x, y), (x + tile, y), 3)
            if cell.walls['right']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), 3)
            if cell.walls['bottom']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x + tile, y + tile), (x, y + tile), 3)
            if cell.walls['left']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x, y + tile), (x, y), 3)
