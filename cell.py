import pygame

from constants import CELL_SIZE


class Cell(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.image, 'white', pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.image, 'black', pygame.Rect(1, 1, CELL_SIZE - 2, CELL_SIZE - 2))
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE, y * CELL_SIZE))
        self.returned = False
        self.flag = False

class NumberedCell(Cell):
    def __init__(self, screen, x, y, number):
        super().__init__(screen, x, y)
        self.number = number

class MinedCell(Cell):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)