import sys

import pygame as pygame
from game import Game

from constants import SCREEN_SIZE

if __name__ == '__main__':
    pygame.init()
    screen_width = SCREEN_SIZE
    screen_height = SCREEN_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()

    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)