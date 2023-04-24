import pygame, sys
from constants import *
from board import Board



def game_start_screen(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    screen.fill(BG_COLOR)

    ##display title
    titledisplay = title_font.render('~~ Sudoku ~~', 1, NUMBER_COLOR)
    titlelocation = titledisplay.get_rect(center=(315, 183))
    screen.blit(titledisplay, titlelocation)

    ##display select difficulty
    instructionsdisplay = button_font.render('Select Difficulty', 1, NUMBER_COLOR)
    instructionslocation = instructionsdisplay.get_rect(center = (315, 300))
    screen.blit(instructionsdisplay, instructionslocation)

    ##print the difficulty buttons
    pygame.draw.rect(screen, BUTTON_COLOR, (35, 350, 140, 70))
    word1 = button_font.render('EASY', 1, NUMBER_COLOR)
    location1 = word1.get_rect(center=(105, 385))
    screen.blit(word1, location1)

    pygame.draw.rect(screen, BUTTON_COLOR, (230, 350, 170, 70))
    word2 = button_font.render('MEDIUM', 1, NUMBER_COLOR)
    location2 = word2.get_rect(center=(315, 385))
    screen.blit(word2, location2)

    pygame.draw.rect(screen, BUTTON_COLOR, (455, 350, 140, 70))
    word3 = button_font.render('HARD', 1, NUMBER_COLOR)
    location3 = word3.get_rect(center=(525, 385))
    screen.blit(word3, location3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if (35 < x < 175) and (350 < y < 420):
                    difficulty_level = 'easy'
                    removed_cells = 30
                    return difficulty_level, removed_cells

                elif (230 < x < 400) and (350 < y < 420):
                    difficulty_level = 'medium'
                    removed_cells = 40
                    return difficulty_level, removed_cells


                elif (455 < x < 595) and (350 < y < 420):
                    difficulty_level = 'hard'
                    removed_cells = 50
                    return difficulty_level, removed_cells
        pygame.display.update()


def you_won(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    screen.fill(BG_COLOR)

    ##display title
    titledisplay = title_font.render('You Won!', 1, NUMBER_COLOR)
    titlelocation = titledisplay.get_rect(center=(315, 183))
    screen.blit(titledisplay, titlelocation)

    ##display subtitle
    instructionsdisplay = button_font.render('IQ = Einstein', 1, NUMBER_COLOR)
    instructionslocation = instructionsdisplay.get_rect(center=(315, 300))
    screen.blit(instructionsdisplay, instructionslocation)

    ##display button
    pygame.draw.rect(screen, BUTTON_COLOR, (230, 350, 170, 70))
    word2 = button_font.render('EXIT', 1, NUMBER_COLOR)
    location2 = word2.get_rect(center=(315, 385))
    screen.blit(word2, location2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if (230 < x < 400) and (350 < y < 420):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def you_lost(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    screen.fill(BG_COLOR)

    ##display title
    titledisplay = title_font.render('You Lost!', 1, NUMBER_COLOR)
    titlelocation = titledisplay.get_rect(center=(315, 183))
    screen.blit(titledisplay, titlelocation)

    ##display subtitle
    instructionsdisplay = button_font.render('IQ = Rock', 1, NUMBER_COLOR)
    instructionslocation = instructionsdisplay.get_rect(center=(315, 300))
    screen.blit(instructionsdisplay, instructionslocation)

    ##display button
    pygame.draw.rect(screen, BUTTON_COLOR, (230, 350, 170, 70))
    word2 = button_font.render('RESTART', 1, NUMBER_COLOR)
    location2 = word2.get_rect(center=(315, 385))
    screen.blit(word2, location2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if (230 < x < 400) and (350 < y < 420):
                    difficulty_level, removed_cells = game_start_screen(screen)
                    return difficulty_level, removed_cells
        pygame.display.update()




