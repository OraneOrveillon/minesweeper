import pygame
import random
from constants import NUMBER_OF_SIDE_CELLS, NUMBER_OF_MINES
from constants import CELL_SIZE, GRID_WIDTH
from constants import GRID_COLOR
from cell import Cell, MinedCell


class Game:
    """
    The top level of the application, represents the game interface.
    """

    def __init__(self, screen):
        """
        - Defines random mines coordinates.
        - For each part of the grid, adds a MinedCell if (i, j) in in mines_coords.
        - If not, draws a normal Cell with a number corresponding to the number of mines around it.

        Args:
            screen (Surface): Top level window.
        """
        # TODO test (enlever après)
        self.iterations = 1000
        self.actual_iteration = 0
        self.screen = screen
        self.cells = []
        self.mines_coords = []
        self.pressed = True
        for i in range(NUMBER_OF_MINES):
            # Same as `do (new mine coords) while`
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
                    cells_around = [(i - 1, j), (i, j - 1), (i - 1, j - 1),
                                    (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)]
                    for cell_coord in cells_around:
                        if self.mines_coords.__contains__(cell_coord):
                            number_of_mines += 1
                    self.cells.append(
                        Cell(self.screen, i, j, number=number_of_mines))

    def draw_grid(self):
        """
        Draws the grid between cells with given grid width dynamically.
        """
        for x in range(NUMBER_OF_SIDE_CELLS):
            for y in range(NUMBER_OF_SIDE_CELLS):
                rect = pygame.Rect(x * (CELL_SIZE + GRID_WIDTH), y *
                                   (CELL_SIZE + GRID_WIDTH), CELL_SIZE + 2 * GRID_WIDTH, CELL_SIZE + 2 * GRID_WIDTH)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, GRID_WIDTH)

    def check_click(self):
        """
        - Checks of clicks by the user.
        - Checks the cell clicked on.
        - Left click : returns the cell.
        - Right click : puts / removes the flag. 
        - Sets pressed to False after methods calls to trigger them only once and sets it to True when the click is released.
        """
        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            for cell in self.cells:
                cell_rect = (cell.rect.x, cell.rect.y)
                # If the click is in the current cell
                if (mouse_pos[0] - cell_rect[0] <= CELL_SIZE) and (mouse_pos[1] - cell_rect[1] <= CELL_SIZE):
                    if pygame.mouse.get_pressed()[0]:
                        if type(cell) == MinedCell:
                            pass
                            # TODO Game over
                        elif cell.number == 0:
                            self.face_up_cells_around(cell.i, cell.j)
                        cell.face_up(self.pressed)
                        self.pressed = False
                    elif pygame.mouse.get_pressed()[2]:
                        cell.set_flag(self.pressed)
                        self.pressed = False
        # If the click is released
        else:
            self.pressed = True

    def face_up_cells_around(self, i, j):
        # TODO docstring
        # FIXME
        print(str(i)+', '+str(j))
        cells_around = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
        for cell_around in cells_around:
            for cell in self.cells:
                if (cell.i, cell.j) == cell_around:
                    if cell.number == 0 and cell.returned == False:
                        cell.face_up(self.pressed)

                        # TODO enlever les 2 lignes d'en-dessous après
                        self.actual_iteration += 1
                        if self.actual_iteration <= self.iterations:
                            self.face_up_cells_around(cell.i, cell.j)
                    break

    def run(self) -> None:
        """
        Draws the cells, the grid and checks of the clicks.
        """
        pygame.sprite.Group(self.cells).draw(self.screen)
        self.draw_grid()
        self.check_click()
