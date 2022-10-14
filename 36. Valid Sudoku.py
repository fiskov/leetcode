# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row: int):
            bfr = [1]*10
            for col in range(9):
                c = board[row][col]
                if c != ".":
                    digit = int(c)
                    if bfr[digit] > 0:
                        bfr[digit] -= 1
                    else:
                        return False
            return True

        def checkCol(col: int):
            bfr = [1]*10
            for row in range(9):
                c = board[row][col]
                if c != ".":
                    digit = int(c)
                    if bfr[digit] > 0:
                        bfr[digit] -= 1
                    else:
                        return False
            return True

        def checkSquare(row: int, col: int):
            bfr = [1]*10
            for i in range(3):
                for j in range(3):
                    c = board[row+i][col+j]
                    if c != ".":
                        digit = int(c)
                        if bfr[digit] > 0:
                            bfr[digit] -= 1
                        else:
                            return False
            return True

        for row in range(9):
            if not checkRow(row):
                return False

        for col in range(9):
            if not checkCol(col):
                return False

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not checkSquare(row, col):
                    return False

        return True


sol = Solution()

print(sol.isValidSudoku(board = \
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))

print(sol.isValidSudoku(board = \
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))
