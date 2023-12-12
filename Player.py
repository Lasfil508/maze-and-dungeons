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
        self.width = player_width
        self.height = player_height
        self.rect = pygame.Rect(x, y, player_width, player_height)

    def update(self, core):
        self.player_physics(core)

    def player_physics(self, core):  # Сделать нормальное передвижение по клеткам
        if self.x_vel == 0 and self.y_vel == 0:
            if core.keyR:
                self.x_vel += speed_increase_rate
                core.keyR = False
            if core.keyL:
                self.x_vel -= speed_increase_rate
                core.keyL = False
            if core.keyU:
                self.y_vel -= speed_increase_rate
                core.keyU = False
            if core.keyD:
                self.y_vel += speed_increase_rate
                core.keyD = False
        else:
            self.x += self.x_vel
            self.y += self.y_vel
            self.rect.x = self.x
            self.rect.y = self.y
            if self.x_vel > 0:
                self.x_vel -= speed_increase_rate
            elif self.x_vel < 0:
                self.x_vel += speed_increase_rate
            if self.y_vel > 0:
                self.y_vel -= speed_increase_rate
            elif self.y_vel < 0:
                self.y_vel += speed_increase_rate

    def render(self, core):
        pygame.draw.circle(core.sc, pygame.Color('yellow'), core.get_map().get_camera().apply(self).topleft, player_width//2)
