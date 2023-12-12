import pygame
from settings import *


class Camera:
    """

    Camera class, for shifting all objects on the screen
    relative to the player.

    """
    # Важно, в будущем передовать ширину и высоту уровня в параметры, т.к. они буду определяться при генерации.
    def __init__(self):
        self.rect = pygame.Rect(0, 0, width, height)
        self.complex_camera(self.rect)

    def complex_camera(self, target_rect):
        x, y = target_rect.x, target_rect.y
        x, y = (-x + width_W / 2 - target_rect.width / 2), (-y + height_W / 2 - target_rect.height)

        x = min(0, x)
        x = max(-(self.rect.width - width_W), x)
        # y = height_W - self.rect.h
        y = max(-(self.rect.height - height_W), y)
        y = min(0, y)

        return pygame.Rect(x, y, self.rect.width, self.rect.height)

    def apply(self, target):
        return target.rect.move(self.rect.topleft)
        # return target.rect.x + self.rect.x, target.rect.y + self.rect.y

    def update(self, target):
        self.rect = self.complex_camera(target)

    def reset(self):
        self.rect = pygame.Rect(0, 0, self.rect.w, self.rect.h)
