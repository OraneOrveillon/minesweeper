import pygame

from constants import CELL_SIZE


class Cell(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self._image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self._image, 'white', pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self._image, 'black', pygame.Rect(1, 1, CELL_SIZE - 2, CELL_SIZE - 2))
        self.rect = self._image.get_rect(topleft=(x * CELL_SIZE, y * CELL_SIZE))
