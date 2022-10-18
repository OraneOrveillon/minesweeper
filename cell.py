import pygame

from constants import CELL_SIZE


class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number=0):
        super().__init__()
        self.screen = screen
        self.number = number
        self.image = pygame.image.load('minesweeper/assets/hidden.png')
        self.rect = self.image.get_rect(topleft=(x * CELL_SIZE + x + 1, y * CELL_SIZE + y + 1))
        self.returned = False
        self.flag = False

    def face_up(self):
        self.returned = True
        self.image = pygame.image.load('minesweeper/assets/'+str(self.number)+'.png')

    def set_flag(self):
        if not self.returned:
            self.flag = not self.flag
            if self.flag: 
                self.image = pygame.image.load('minesweeper/assets/flag.png')
            else: 
                self.image = pygame.image.load('minesweeper/assets/hidden.png')

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # Left click
            if pygame.mouse.get_pressed()[0]:
                self.face_up()
            elif pygame.mouse.get_pressed()[2]:
                self.set_flag()


class MinedCell(Cell):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    def face_up(self):
        self.returned = True
        self.image = pygame.image.load('minesweeper/assets/mine.png')
