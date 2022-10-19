import pygame

from constants import CELL_SIZE


class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number=0):
        super().__init__()
        self.screen = screen
        self.number = number
        # TODO : refactoriser les chemin + monter le projet d'un niveau de répertoire
        self.image = pygame.image.load('minesweeper/assets/hidden.png')
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE + x + 1, y * CELL_SIZE + y + 1))
        self.flag = False

    def face_up(self):
        self.returned = True
        self.image = pygame.image.load('minesweeper/assets/'+str(self.number)+'.png')

    def set_flag(self):
        self.flag = not self.flag
        if self.flag: 
            self.image = pygame.image.load('minesweeper/assets/flag.png')
        else: 
            self.image = pygame.image.load('minesweeper/assets/hidden.png')


class MinedCell(Cell):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    def face_up(self):
        self.returned = True
        self.image = pygame.image.load('minesweeper/assets/mine.png')
