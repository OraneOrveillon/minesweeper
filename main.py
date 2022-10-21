import sys

import pygame as pygame
from game import Game

from constants import SCREEN_SIZE, FPS

if __name__ == '__main__':
    """
    - Initializes pygame.
    - Sets window size and title.
    - Initializes the clock.
    - Instantiates the game.
    - Loops the run method with the given FPS in the clock ticking.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()

    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        game.run()

        pygame.display.flip()
        clock.tick(FPS)