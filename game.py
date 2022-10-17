import pygame
import random
from constants import NUMBER_OF_SIDE_CELLS, NUMBER_OF_MINES
from cell import Cell, MinedCell

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.cells = []
        self.mines_coords = []
        for i in range(NUMBER_OF_MINES):
            # Same as `do (new mine coords) while `
            while True:
                mine_coords = (random.randint(0, NUMBER_OF_SIDE_CELLS - 1),
                               random.randint(0, NUMBER_OF_SIDE_CELLS - 1))
                if not self.mines_coords.__contains__(mine_coords):
                    break
            self.mines_coords.append(mine_coords)

        # Draw cells and mines
        for i in range(NUMBER_OF_SIDE_CELLS):
            for j in range(NUMBER_OF_SIDE_CELLS):
                if self.mines_coords.__contains__((i, j)):
                    self.cells.append(MinedCell(self.screen, i, j))
                else:
                  # Add numbered cells
                  number_of_mines = 0
                  # Cells around the actual cell
                  range_cells = [(i - 1, j), (i, j - 1), (i - 1, j-1),
                                (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)]
                  for cell_coord in range_cells:
                    if self.mines_coords.__contains__(cell_coord):
                      number_of_mines += 1
                  self.cells.append(Cell(self.screen, i, j , number=number_of_mines))
       

    def run(self) -> None:
        pygame.sprite.Group(self.cells).draw(self.screen)
