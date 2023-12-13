import pygame
from settings import *


class Player:
    """

    Player class, handles the player's physics, collision, and display.

    """
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.x_vel = 0
        self.y_vel = 0
        self.step = 0
        self.width = player_width
        self.height = player_height
        self.rect = pygame.Rect(x, y, player_width, player_height)

    def update(self, core):
        self.player_physics(core)

    def player_physics(self, core):
        if self.x_vel == 0 and self.y_vel == 0:
            if core.keyR and self.collizion(core, 1):
                self.x_vel += speed_increase_rate
                core.keyR = False
            elif core.keyL and self.collizion(core, 3):
                self.x_vel -= speed_increase_rate
                core.keyL = False
            elif core.keyU and self.collizion(core, 0):
                self.y_vel -= speed_increase_rate
                core.keyU = False
            elif core.keyD and self.collizion(core, 2):
                self.y_vel += speed_increase_rate
                core.keyD = False
        else:
            self.x += self.x_vel
            self.rect.x = self.x
            self.y += self.y_vel
            self.rect.y = self.y
            self.step += 1

            if self.step == 6:
                core.get_map().current_cell = self.y//tile, self.x//tile
                self.x_vel = 0
                self.y_vel = 0
                self.step = 0

    def collizion(self, core, direction):
        if direction == 0 and core.get_map().grid_cells[core.get_map().current_cell[0]][core.get_map().current_cell[1]].walls['top']:
            return True
        elif direction == 1 and core.get_map().grid_cells[core.get_map().current_cell[0]][core.get_map().current_cell[1]].walls['right']:
            return True
        elif direction == 2 and core.get_map().grid_cells[core.get_map().current_cell[0]][core.get_map().current_cell[1]].walls['bottom']:
            return True
        elif direction == 3 and core.get_map().grid_cells[core.get_map().current_cell[0]][core.get_map().current_cell[1]].walls['left']:
            return True
        return False


    def render(self, core):
        pygame.draw.circle(core.sc, pygame.Color('yellow'), core.get_map().get_camera().apply(self).topleft, player_width//2)
