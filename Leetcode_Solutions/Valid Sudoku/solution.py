def is_valid(self, l):
        l = [i for i in l if i != '.']
        return len(set(l)) == len(l)
        
    def is_row_valid(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        return True
        
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(square):
                    return False
        return True

    def isValidSudoku(self, board):
        return (self.is_row_valid(board) &
            self.is_col_valid(board) &
            self.is_square_valid(board))
