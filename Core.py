import pygame
from settings import *
from Cell import Cell
from MazeGenerator import MazeGenerator
from Map import Map
from MenuManager import MenuManager


class Core:
    def __init__(self):
        pygame.init()

        self.sc = pygame.display.set_mode(size)
        pygame.display.set_caption('Maze & Dungeons')

        self.clock = pygame.time.Clock()

        self.grid_cells = [Cell(self.sc, col, row) for row in range(rows) for col in range(cols)]
        self.mazeGenerator = MazeGenerator(self.grid_cells)
        self.map = Map(self.grid_cells)
        self.oMM = MenuManager()

        self.mazeGenerator.generateMaze()

        self.run = True

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def main_loop(self):
        while self.run:
            self.input()
            self.sc.fill((0, 0, 0))
            self.map.render()

            pygame.display.flip()
            self.clock.tick(fps)

        pygame.quit()

    def get_map(self):
        return self.map


