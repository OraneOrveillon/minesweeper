import pygame

from constants import CELL_SIZE

class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, color='black'):
        super().__init__()
        self.screen = screen
        self.number = number
        self.image = image or pygame.image.load('minesweeper/assets/'+str(number)+'.png')
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE, y * CELL_SIZE))
        self.returned = False
        self.flag = False

class NumberedCell(Cell):
    def __init__(self, screen, x, y, number):
        super().__init__(screen, x, y)
        self.number = number

class MinedCell(Cell):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, color='red')