class Sudoku:
    def solveSudoko(self, matrix):
        self.matirx = matrix
        self.solve()

    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        for num in [str(i) for i in range(1, 10)]:
            if self.canFill(row, col, num):
                self.matirx[row][col] = num
                if self.solve():
                    return True
                self.matirx[row][col] = '.'
        return False

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.matirx[row][col] == ".":
                    return row, col
        return -1, -1

    def canFill(self, row, col, T):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkRow(row, T) and self.checkCol(col, T) and self.checkSqure(boxrow, boxcol, T):
            return True
        return False

    def checkRow(self, row, T):
        for col in range(9):
            if self.matirx[row][col] == T:
                return False
        return True

    def checkCol(self, col, T):
        for row in range(9):
            if self.matirx[row][col] == T:
                return False
        return True

    def checkSqure(self, row, col, T):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.matirx[r][c] == T:
                    return False
        return True

if __name__ == "__main__":
    matrix = []
    with open('task_1_input.txt') as f:
        for i in f.readlines():
            matrix.append(i.split())
    ans = Sudoku()
    ans.solveSudoko(matrix)
    for line in matrix:
        print(line)
