import pygame


class MenuManager:
    def __init__(self):
        self.currentGameState = 'Game'

    def update(self, core):
        if self.currentGameState == 'Game':
            core.get_map().render()

