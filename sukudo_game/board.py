
from constants import *
import pygame
class Board:
  def __init__(self, width, height, screen, difficulty, original):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.original = original

  def draw(self):
        """Draw the Sudoku grid with lines and cells."""
        self.screen.fill(WHITE)
        for i in range(10):
            line_width = BOLD_WIDTH if i % 3 == 0 else THIN_WIDTH
            pygame.draw.line(self.screen, BLACK, (0, SQUARE_SIZE * i), (self.width, SQUARE_SIZE * i), line_width)
            pygame.draw.line(self.screen, BLACK, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, self.height), line_width)

  def select(self, row, col, removed_cells):
    if row == None:
      return
    if col == None:
      return
    if row > 9:
      return
    id = (row * 9) + col
    if id not in removed_cells:
      return
    start_coordinate_top = ((SQUARE_SIZE * col) + 4, (SQUARE_SIZE * row) + 4)
    end_coordinate_top = ((SQUARE_SIZE * (col + 1)) - 4, (SQUARE_SIZE * row) + 4)
    start_coordinate_bottom = ((SQUARE_SIZE * col) + 4, (SQUARE_SIZE * (row + 1)) - 4)
    end_coordinate_bottom = ((SQUARE_SIZE * (col + 1)) - 4, ((SQUARE_SIZE * (row + 1)) - 4))

    # Horizontal lines
    pygame.draw.line(self.screen, RED, start_coordinate_top, end_coordinate_top, HIGHLIGHT_WIDTH)
    pygame.draw.line(self.screen, RED, start_coordinate_bottom, end_coordinate_bottom, HIGHLIGHT_WIDTH)

    # Vertical lines
    pygame.draw.line(self.screen, RED, start_coordinate_top, start_coordinate_bottom, HIGHLIGHT_WIDTH)
    pygame.draw.line(self.screen, RED, end_coordinate_top, end_coordinate_bottom, HIGHLIGHT_WIDTH)

  def click(self, x, y):
    x = x // SQUARE_SIZE
    if y > 450:
      return None
    else:
      y = y // SQUARE_SIZE

    return (x, y)

  def click(self, x, y):
        """Determine which cell was clicked based on screen coordinates."""
        if y > 450:
            return None
        return x // SQUARE_SIZE, y // SQUARE_SIZE
    
   


  def reset_to_original(self, cell_list):
    for row_num, row in enumerate(cell_list):
      for col_num, cell in enumerate(row):
        cell.set_cell_value(self.original[row_num][col_num])
        cell.set_sketched_value(0)

    return True

  def is_full(self, cell_list):
        """Check if the board is completely filled."""
        return all(cell.value != 0 for row in cell_list for cell in row)

  def valid_in_row(self, row, num, cell_list):
        """Validate if a number is valid in the specified row."""
        return sum(cell.value == num for cell in cell_list[row]) == 1

  def valid_in_col(self, col, num, cell_list):
        """Validate if a number is valid in the specified column."""
        return sum(row[col].value == num for row in cell_list) == 1

  def valid_in_box(self, row_start, col_start, num, cell_list):
        """Validate if a number is valid in the specified 3x3 box."""
        return sum(cell_list[i][j].value == num for i in range(row_start, row_start+3) for j in range(col_start, col_start+3)) == 1
  def check_board(self, cell_list):
        """Check if the board is solved correctly."""
        for row_num, row in enumerate(cell_list):
            for col_num, cell in enumerate(row):
                num = cell.value
                row_start = (row_num // 3) * 3
                col_start = (col_num // 3) * 3
                if not (self.valid_in_row(row_num, num, cell_list) and
                        self.valid_in_col(col_num, num, cell_list) and
                        self.valid_in_box(row_start, col_start, num, cell_list)):
                    return False
        return True
