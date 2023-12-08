import pygame
from settings import *


def main():
    pygame.init()
    sc = pygame.display.set_mode(size)
    pygame.display.set_caption('Maze & Dungeons')
    clock = pygame.time.Clock()

    run = True
    while run:
        sc.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

if __name__ == '__main__':
    main()