import pygame
from settings import *
from Cell import Cell


def main():
    pygame.init()
    sc = pygame.display.set_mode(size)
    pygame.display.set_caption('Maze & Dungeons')
    clock = pygame.time.Clock()

    grid_cells = [Cell(sc, col, row) for row in range(rows) for col in range(cols)]

    run = True
    while run:
        sc.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        [cell.draw() for cell in grid_cells]

        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

if __name__ == '__main__':
    main()
