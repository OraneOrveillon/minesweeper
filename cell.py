import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()
        self.size = 20
        self.screen = screen
        self._image = pygame.Surface((20, 20))
        pygame.draw.rect(self._image, 'white', pygame.Rect(0, 0, self.size, self.size))
        pygame.draw.rect(self._image, 'black', pygame.Rect(1, 1, self.size - 2, self.size - 2))
        self.rect = self._image.get_rect(topleft=(x * self.size, y * self.size))
