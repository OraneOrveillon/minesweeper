import pygame
import random
from constants import NUMBER_OF_SIDE_CELLS, NUMBER_OF_MINES, CELL_SIZE, GRID_COLOR, GRID_WIDTH
from cell import Cell, MinedCell


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.cells = []
        self.mines_coords = []
        self.pressed = True
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
                    self.cells.append(
                        Cell(self.screen, i, j, number=number_of_mines))

    def draw_grid(self):
        for x in range(NUMBER_OF_SIDE_CELLS):
            for y in range(NUMBER_OF_SIDE_CELLS):
                rect = pygame.Rect(x * (CELL_SIZE + GRID_WIDTH), y *
                                   (CELL_SIZE + GRID_WIDTH), CELL_SIZE + 2 * GRID_WIDTH, CELL_SIZE + 2 * GRID_WIDTH)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, GRID_WIDTH)

    def check_click(self):
        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            for cell in self.cells:
                cell_rect = (cell.rect.x, cell.rect.y)
                # If the click is in the current cell
                if (mouse_pos[0] - cell_rect[0] <= CELL_SIZE) and (mouse_pos[1] - cell_rect[1] <= CELL_SIZE):
                    if pygame.mouse.get_pressed()[0]:
                        cell.face_up(self.pressed)
                        self.pressed = False
                    elif pygame.mouse.get_pressed()[2]:
                        cell.set_flag(self.pressed)
                        self.pressed = False
        # If the click is released
        else:
            self.pressed = True

    def run(self) -> None:
        pygame.sprite.Group(self.cells).draw(self.screen)
        self.draw_grid()
        self.check_click()
