import pygame
from settings import *


class Cell:
    def __init__(self, sc, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
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
