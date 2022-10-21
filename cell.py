import pygame

from constants import CELL_SIZE, GRID_WIDTH


class Cell(pygame.sprite.Sprite):
    """
    One item of the game grid.
    """
    def __init__(self, screen, x, y, number=0):
        """
        Initializes a sprite cell that is hidden at the start of the game.

        Args:
            screen (Surface): Top level window.
            x (int): i position in the matrix of cells.
            y (int): j position in the matrix of cells.
            number (int, optional): _description_. Defaults to 0.
        """
        super().__init__()
        self.screen = screen
        self.number = number
        self.returned = False
        self.image = pygame.image.load('assets/hidden.png')
        self.face_up_image = pygame.image.load(f'assets/{str(self.number)}.png')
        self.rect = self.image.get_rect(topleft=(x * (CELL_SIZE + GRID_WIDTH) + GRID_WIDTH, y * (CELL_SIZE + GRID_WIDTH) + GRID_WIDTH))
        self.flag = False

    def face_up(self, pressed):
        """
        Returns the cell.

        Args:
            pressed (bool): If the click is active.
        """
        if pressed:
            self.returned = True
            self.image = self.face_up_image

    def set_flag(self, pressed):
        """
        Toggles the flag is the cells is not returned.

        Args:
            pressed (bool): If the click is active.
        """
        if pressed and not self.returned:
            self.flag = not self.flag
            if self.flag: 
                self.image = pygame.image.load('assets/flag.png')
            else: 
                self.image = pygame.image.load('assets/hidden.png')


class MinedCell(Cell):
    """
    A cell but with a mine on it.
    """
    def __init__(self, screen, x, y):
        """
        Initializes a cell but with a different image.

        Args:
            See Cell class.
        """
        super().__init__(screen, x, y)
        self.face_up_image = pygame.image.load('assets/mine.png')
