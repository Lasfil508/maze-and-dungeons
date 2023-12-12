import pygame


class MenuManager:
    """

    A class for handling game states. Updates and displays different things.

    """
    def __init__(self):
        self.currentGameState = 'Game'

    def update(self, core):
        if self.currentGameState == 'Game':
            core.get_map().update()

    def render(self, core):
        if self.currentGameState == 'Game':
            core.get_map().render()
