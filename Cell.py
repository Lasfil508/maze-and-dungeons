import pygame
from settings import *


class Cell:
    """

    A class for convenient realization of the game field cells and
    convenient generation of the maze

    """
    def __init__(self, sc, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.rect = pygame.Rect(x*tile, y*tile, tile, tile)
        self.visited = False
        self.sc = sc

    def draw(self):
        x, y = self.x * tile, self.y * tile
        if self.visited:
            pygame.draw.rect(self.sc, pygame.Color('black'), (x, y, tile, tile))

        if self.walls['top']:
            pygame.draw.line(self.sc, pygame.Color('darkorange'), (x, y), (x + tile, y), 3)
        if self.walls['right']:
            pygame.draw.line(self.sc, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), 3)
        if self.walls['bottom']:
            pygame.draw.line(self.sc, pygame.Color('darkorange'), (x + tile, y + tile), (x, y + tile), 3)
        if self.walls['left']:
            pygame.draw.line(self.sc, pygame.Color('darkorange'), (x, y + tile), (x, y), 3)

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return find_index(x, y)
