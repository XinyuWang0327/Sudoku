# Cell Class
import pygame
import board as Board

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (252, 3, 3)
GREY = (162, 162, 162)
WIDTH = 450
BOARD_LENGTH = 450
SCREEN_LENGTH = 525
THIN_WIDTH = 5
BOLD_WIDTH = 10
HIGHLIGHT_WIDTH = 3
SQUARE_SIZE = WIDTH / 9



class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.sketched_value = 0

  def set_cell_value(self, value):
    if value <= 9:
      self.value = value

  def set_sketched_value(self, value):
    self.sketched_value = value
          
  def sketch_num(self, row, col, screen):
    if self.value > 0:
            font = pygame.font.Font(None, 40)
            value_text = font.render(str(self.value), True, BLACK)
            value_rect = value_text.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                                                     SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(value_text, value_rect)

  # user inputed numbers
  def sketch_sketched_num(self, row, col, screen):
    if self.sketched_value == 0:
      return
    small_font = pygame.font.Font(None, 20)
    cell_surf = small_font.render(str(self.sketched_value), 0, GREY)
    cell_rect = cell_surf.get_rect(center=(50 * (col) + 12, 50 * (row) + 12))
    screen.blit(cell_surf, cell_rect)
    

  def __repr__(self):
    return self.value
    