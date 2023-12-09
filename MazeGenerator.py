import pygame
from random import choice
from settings import *


class MazeGenerator:
    def __init__(self, grid_cells):
        self.grid_cells = grid_cells
        self.current_cell = self.grid_cells[cols*(rows//2)-rows//2]
        self.stack = []

    def generateMaze(self):
        while self.check_visited_cells():
            self.current_cell.visited = True
            next_cell = self.check_neighbors()
            if next_cell:
                next_cell.visited = True
                self.stack.append(self.current_cell)
                self.remove_walls(self.current_cell, next_cell)
                self.current_cell = next_cell
            elif self.stack:
                self.current_cell = self.stack.pop()

    def remove_walls(self, current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    def check_neighbors(self):
        neighbors = []
        top = self.grid_cells[self.current_cell.check_cell(self.current_cell.x, self.current_cell.y - 1)]
        right = self.grid_cells[self.current_cell.check_cell(self.current_cell.x + 1, self.current_cell.y)]
        bottom = self.grid_cells[self.current_cell.check_cell(self.current_cell.x, self.current_cell.y + 1)]
        left = self.grid_cells[self.current_cell.check_cell(self.current_cell.x - 1, self.current_cell.y)]
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

    def check_visited_cells(self):
        for cell in self.grid_cells:
            if not cell.visited:
                return True
        return False
