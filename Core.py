import pygame
from settings import *
from Cell import Cell
from MazeGenerator import MazeGenerator
from Map import Map
from MenuManager import MenuManager


class Core:
    """

    Main class

    """
    def __init__(self):
        pygame.init()

        self.sc = pygame.display.set_mode(size_W)
        pygame.display.set_caption('Maze & Dungeons')

        self.clock = pygame.time.Clock()

        self.grid_cells = [Cell(self.sc, col, row) for row in range(rows) for col in range(cols)]
        self.mazeGenerator = MazeGenerator(self.grid_cells)
        self.map = Map(self.grid_cells)
        self.oMM = MenuManager()

        self.mazeGenerator.generateMaze()

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False

    def input(self):
        if self.get_mm().currentGameState == 'Game':
            self.input_player()

    def input_player(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.keyR = True
                elif event.key == pygame.K_LEFT:
                    self.keyL = True
                elif event.key == pygame.K_UP:
                    self.keyU = True
                elif event.key == pygame.K_DOWN:
                    self.keyD = True

    def main_loop(self):
        while self.run:
            self.input()
            self.sc.fill((0, 0, 0))
            self.get_mm().update(self)
            self.get_mm().render(self)

            pygame.display.flip()
            self.clock.tick(fps)

        pygame.quit()

    def get_map(self):
        return self.map

    def get_mm(self):
        return self.oMM
