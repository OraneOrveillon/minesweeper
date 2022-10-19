import pygame

from constants import CELL_SIZE, GRID_WIDTH


class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number=0):
        super().__init__()
        self.screen = screen
        self.number = 0
        self.image = pygame.image.load('assets/hidden.png')
        self.face_up_image = pygame.image.load(f'assets/{str(self.number)}.png')
        self.rect = self.image.get_rect(topleft=(x * (CELL_SIZE + GRID_WIDTH) + GRID_WIDTH, y * (CELL_SIZE + GRID_WIDTH) + GRID_WIDTH))
        self.flag = False

    def face_up(self, pressed):
        if pressed:
            self.returned = True
            self.image = self.face_up_image

    def set_flag(self, pressed):
        if pressed:
            self.flag = not self.flag
            if self.flag: 
                self.image = pygame.image.load('assets/flag.png')
            else: 
                self.image = pygame.image.load('assets/hidden.png')


class MinedCell(Cell):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.face_up_image = pygame.image.load('assets/mine.png')
