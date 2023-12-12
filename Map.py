import pygame
from settings import *
from Camera import Camera
from Player import Player


class Map:
    """

    A class for displaying and storing game objects on the map.

    """

    def __init__(self, grid_cells):
        self.grid_cells = grid_cells.copy()
        self.obj = []
        self.mobs = []
        self.camera = Camera()
        self.player = Player(35, 35)

    def update(self, core):
        self.get_player().update(core)
        self.get_camera().update(self.get_player())

    def get_player(self):
        return self.player

    def get_camera(self):
        return self.camera

    def render(self, core):
        for cell in self.grid_cells:
            x, y = self.get_camera().apply(cell).topleft
            # x, y = x-width//2+width_W//2, y-height//2+height_W//2
            # pygame.draw.rect(cell.sc, pygame.Color('darkgrey'), (x, y, tile, tile), 1)

            if cell.walls['top']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x, y), (x + tile, y), 3)
            if cell.walls['right']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), 3)
            if cell.walls['bottom']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x + tile, y + tile), (x, y + tile), 3)
            if cell.walls['left']:
                pygame.draw.line(cell.sc, pygame.Color('darkorange'), (x, y + tile), (x, y), 3)
        self.get_player().render(core)
