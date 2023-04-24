import pygame, sys
from constants import *


import pygame
pygame.init()
word_font = pygame.font.Font(None, 50)



class Board():
    def __init__(self, screen, difficulty, width = 600 , height = 600,):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        ### draw horizontal lines
        for i in range (1, BOARD_ROWS + 1):
            if i % 3 == 0:
                line_width = LINE_WIDTH_THICK
            else:
                line_width = LINE_WIDTH_THIN
            pygame.draw.line(self.screen, LINE_COLOR, (0, i*SQUARE_SIZE), (WIDTH, i*SQUARE_SIZE), line_width)

        ### draw vertical lines
        for i in range(1, BOARD_ROWS):
            if i % 3 == 0:
                line_width = LINE_WIDTH_THICK
            else:
                line_width = LINE_WIDTH_THIN
            pygame.draw.line(self.screen, LINE_COLOR, (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, 630), line_width)

        ##draw buttons at buttom
        pygame.draw.rect(self.screen, BUTTON_COLOR, (35, 645, 140, 70))
        word1 = word_font.render('RESET', 1, NUMBER_COLOR)
        location1 = word1.get_rect(center=(105,680))
        self.screen.blit(word1, location1)

        pygame.draw.rect(self.screen, BUTTON_COLOR, (230, 645, 170, 70))
        word2 = word_font.render('RESTART', 1, NUMBER_COLOR)
        location2 = word2.get_rect(center=(315, 680))
        self.screen.blit(word2, location2)

        pygame.draw.rect(self.screen, BUTTON_COLOR, (455, 645, 140, 70))
        word3 = word_font.render('EXIT', 1, NUMBER_COLOR)
        location3 = word3.get_rect(center=(525, 680))
        self.screen.blit(word3, location3)


    def select(self, row, col):
        pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE),(col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH_THICK)
        pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE),((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), LINE_WIDTH_THICK)
        pygame.draw.line(self.screen, RED, ((col+1)*SQUARE_SIZE,row*SQUARE_SIZE),((col+1)*SQUARE_SIZE,(row+1)*SQUARE_SIZE), LINE_WIDTH_THICK)
        pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE, (row+1) * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE,(row + 1) * SQUARE_SIZE), LINE_WIDTH_THICK)


    def click(self, x, y):
        ##determines what row and column you clicked in
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def clear(self):
        pass

    def sketch(self, value):
        pass


    def place_number(self, value):
        pass


    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass






