import pygame, sys
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from extrascreens import game_start_screen
from extrascreens import you_won
from extrascreens import you_lost





if __name__ == '__main__':



    sketch_font = pygame.font.Font(None, 20)


    ##the sodoku template


    pygame.init()
    pygame.display.set_caption('Sudoku')
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

    ##start screen
    difficulty_level, removed_cells = game_start_screen(screen)



    board = Board(screen, difficulty_level)
    screen.fill(BG_COLOR)

    ## draw the lines on the board
    board.draw()


    currboard, realboard, boardwzeroes = generate_sudoku(9, removed_cells)



    for rows in range(0, 9):
        for cols in range(0, 9):
            currvalue = currboard[rows][cols]
            if currvalue != 0:
                cell = Cell(currvalue, rows, cols, screen)
                cell.draw()


    ## draw the lines on the board
    board.draw()
    sketched_values = []

    while True:
        for event in pygame.event.get():

            ##exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ##when you click on mousepad
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos

                ##when you click the buttons on the bottom
                if (35 < x < 175 ) and (645 < y < 715):
                    ###reset the game
                    for rows in range(0, 9):
                        for cols in range(0, 9):
                            currboard[rows][cols] = boardwzeroes[rows][cols]
                    sketched_values = []

                if (230 < x < 400) and (654 < y < 715):
                    difficulty_level, removed_cells = game_start_screen(screen)
                    currboard, realboard, boardwzeroes = generate_sudoku(9, removed_cells)

                if (455 < x < 595) and (645 < y < 715):
                    pygame.quit()
                    sys.exit()




                row, col = board.click(x, y)

                if row < 9 and col < 9:
                    board.select(row, col)

                ##start of the board redrawing code
                screen.fill(BG_COLOR)
                board.draw()

                for rows in range(0, 9):
                    for cols in range(0, 9):
                        currvalue = currboard[rows][cols]
                        if currvalue != 0:
                            cell = Cell(currvalue, rows, cols, screen)
                            cell.draw()

                for sketched_nums in sketched_values:
                    sketch_num_draw = sketch_font.render(sketched_nums[0], True, SKETCH_COLOR)
                    screen.blit(sketch_num_draw,
                                ((sketched_nums[1] * SQUARE_SIZE) + 10, (sketched_nums[2] * SQUARE_SIZE) + 10))

                if row < 9 and col < 9:
                    board.select(row, col)

                ##end of board redrawing code

            ##when you hit a key
            if event.type == pygame.KEYDOWN:

                ##when you hit the backspace key
                if event.key == pygame.K_BACKSPACE:
                    for sketched_nums in sketched_values:
                        if sketched_nums[1] == col and sketched_nums[2] == row:
                            sketched_values.remove( sketched_nums )


                    if boardwzeroes[row][col] == 0 and currboard[row][col] != 0:
                        currboard[row][col] = 0



                ##when you hit the return key
                elif event.key == pygame.K_RETURN:
                    for sketched_nums in sketched_values:
                        if sketched_nums[1] == col and sketched_nums[2] == row:
                            currboard[row][col] = int(sketched_nums[0])
                            sketched_values.remove(sketched_nums)

                    board.select(row, col)

                ##when you hit the arrows
                elif event.key == pygame.K_UP:
                    if row > 0:
                        row -= 1

                elif event.key == pygame.K_DOWN:
                    if row < 8:
                        row += 1

                elif event.key == pygame.K_RIGHT:
                    if col < 8:
                        col += 1

                elif event.key == pygame.K_LEFT:
                    if col > 0:
                        col -= 1


                else:
                    sketch_num = ''
                    sketch_num += event.unicode

                    if boardwzeroes[row][col] == 0:

                        ## draw sketched number
                        sketch_num_draw = sketch_font.render(sketch_num, True, SKETCH_COLOR)
                        screen.blit(sketch_num_draw, ( (col * SQUARE_SIZE)+10, (row * SQUARE_SIZE) + 10))
                        sketched_values.append( [sketch_num, col, row ] )

                ##start of board drawing code
                screen.fill(BG_COLOR)
                board.draw()

                for rows in range(0, 9):
                    for cols in range(0, 9):
                        currvalue = currboard[rows][cols]
                        if currvalue != 0:
                            cell = Cell(currvalue, rows, cols, screen)
                            cell.draw()

                for sketched_nums in sketched_values:
                    sketch_num_draw = sketch_font.render(sketched_nums[0], True, SKETCH_COLOR)
                    screen.blit(sketch_num_draw,
                                ((sketched_nums[1] * SQUARE_SIZE) + 10, (sketched_nums[2] * SQUARE_SIZE) + 10))

                if row < 9 and col < 9:
                    board.select(row, col)
                ##end of board drawing code


        ##checks if the board is completed or not
        keepgoing = False
        for rows in range(0, 9):
            for cols in range(0, 9):
                if currboard[rows][cols] == 0:
                    keepgoing = True


        ##if the board is completed, checks it if its right or not
        while keepgoing == False:

            for rows in range(0,9):
                for cols in range(0,9):
                    if currboard[rows][cols] != realboard[rows][cols]:
                        difficulty_level, removed_cells = you_lost(screen)
                        didyouwin = False
                        currboard, realboard, boardwzeroes = generate_sudoku(9, removed_cells)

                        ##board drawing code
                        screen.fill(BG_COLOR)
                        for rows in range(0, 9):
                            for cols in range(0, 9):
                                currvalue = currboard[rows][cols]
                                if currvalue != 0:
                                    cell = Cell(currvalue, rows, cols, screen)
                                    cell.draw()

                        ## draw the lines on the board
                        board.draw()
                        sketched_values = []
                        ##end board drawing code

                        keepgoing = True
                        break

                    if keepgoing == True:
                        break

                if keepgoing == True:
                    break

            if keepgoing == True:
                break

            else:
                you_won(screen)


        pygame.display.update()

    main()