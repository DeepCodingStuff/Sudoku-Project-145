import math, random



class SudokuGenerator:

    ##initializes class
    def __init__(self, row_length = 9, removed_cells = 30):
        self.row_length = row_length
        self.box_length = 3
        self.removed_cells = removed_cells
        self.board = []
        for num in range(0, row_length):
            self.board.append( [] )
            for nums in range(0, row_length):
                self.board[num].append(0)


    ##return the self.board
    def get_board(self):
        return self.board


    def print_board(self):
        print(self.board)


    ##checks if the number appears elsewehere in the row
    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    ##checks if the number appears elsewehere in the col
    def valid_in_col(self, col, num):
        for rows in self.board:
            if rows[col] == num:
                return False
        return True

    ##checks if the number appears elsewehere in the box
    def valid_in_box(self, row_start, col_start, num):
        for rows in range(row_start, row_start + 3):
            for cols in range(col_start, col_start + 3):
                if self.board[rows][cols] == num:
                    return False
        return True


    ##checks if the number is valid in the board
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) == False:
            return False
        if self.valid_in_col(col, num) == False:
            return False

        if row < 3:
            row_start = 0
        if row >= 3 and row < 6:
            row_start = 3
        if row >= 6:
            row_start = 6

        if col < 3:
            col_start = 0
        if col >= 3 and col < 6:
            col_start = 3
        if col >= 6:
            col_start = 6

        if self.valid_in_box(row_start, col_start, num) == False:
            return False

        return True



    ##fills one of the 3x3 boxes
    def fill_box(self, row_start, col_start):
        for rows in range(row_start, row_start + 3):
            for cols in range(col_start, col_start + 3):
                is_it_valid = False
                while is_it_valid == False:
                    new_num = random.randint(1, 9)
                    is_it_valid = self.valid_in_box(row_start, col_start, new_num)
                self.board[rows][cols] = new_num



    ##fills the three diagonal boxes
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
        realboard = self.board
        return realboard



    ##fills the remaining boxes
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.fill_remaining(row, col + 1):
                    return True

                self.board[row][col] = 0
        return False



    ##fills a value in the board
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0,0)
        # for rows in range(0, 3):
        #     for cols in range(3, 9):
        #         if self.board[rows][cols] == 0:
        #             self.fill_remaining(rows, cols)
        #
        #
        # for rows in range(3, 6):
        #     for cols in range(0,3):
        #         while self.board[rows][cols] == 0:
        #             self.fill_remaining(rows, cols)
        #     for cols in range(6, 9):
        #         while self.board[rows][cols] == 0:
        #             self.fill_remaining(rows, cols)
        #
        # for rows in range(6, 9):
        #     for cols in range(0, 6):
        #         while self.board[rows][cols] == 0:
        #             self.fill_remaining(rows, cols)

        realboard = []
        for rows in range(0, 9):
            realboard.append( [] )
            for cols in range(0,9):
                realboard[rows].append(self.board[rows][cols])

        return realboard



    ##removes the designated cells
    def remove_cells(self):
        removedcells = self.removed_cells
        while removedcells > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removedcells -= 1
        boardwzeroes = []
        for rows in range(0, 9):
            boardwzeroes.append( [] )
            for cols in range(0,9):
                boardwzeroes[rows].append(self.board[rows][cols])
        return boardwzeroes




##generates the full board
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    realboard = sudoku.fill_values()
    boardwzeroes = sudoku.remove_cells()
    currboard = sudoku.get_board()
    return currboard, realboard, boardwzeroes
