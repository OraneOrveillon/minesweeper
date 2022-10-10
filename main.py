import sys

import pygame as pygame
from game import Game

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

if __name__ == '__main__':
    pygame.init()
    screen_width = SCREEN_WIDTH
    screen_height = SCREEN_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
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
