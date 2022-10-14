# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        a = [[0 for i in range(n)] for j in range(m)]

        for coord in indices:
            for i in range(n):
                a[coord[0]][i] += 1
            for j in range(m):
                a[j][coord[1]] += 1

        odd_count = 0
        for row in a:
            for cell in row:
                if cell % 2 == 1:
                    odd_count += 1

        return odd_count


sol = Solution()

print(sol.oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(sol.oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))
