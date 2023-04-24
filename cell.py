
import pygame, sys
from constants import *

pygame.init()
number_font = pygame.font.Font(None, 70)
sketch_font = pygame.font.Font(None, 20)


class Cell():
    def __init__(self, value, row, col, screen):
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.realvalue = value


    def draw(self):
        ##draws the number on the board

        thing_to_draw = number_font.render(self.value, 1, NUMBER_COLOR)

        x_cord = (self.col * SQUARE_SIZE) + (SQUARE_SIZE/2)
        y_cord = (self.row * SQUARE_SIZE) + (SQUARE_SIZE/2)
        num_location = thing_to_draw.get_rect(center = (x_cord, y_cord))
        self.screen.blit(thing_to_draw, num_location)



