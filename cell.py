import pygame

from constants import CELL_SIZE


class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number=0, image=None):
        super().__init__()
        self.screen = screen
        self.number = number
        self.image = image or pygame.image.load(
            'minesweeper/assets/'+str(number)+'.png')
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE, y * CELL_SIZE))
        self.returned = False
        self.flag = False


class MinedCell(Cell):
    def __init__(self, screen, x, y):
        image = pygame.image.load('minesweeper/assets/mine.png')
        super().__init__(screen, x, y, image=image)
