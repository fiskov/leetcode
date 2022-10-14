# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# leet_118

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            bfr = [1]
            for j in range(i-1):
                bfr.append(res[i-1][j] + res[i-1][j+1])
            bfr.append(1)
            res.append(bfr)
        return res


sol = Solution()

print(sol.generate(5))   # 5
print(sol.generate(1))   # 1
