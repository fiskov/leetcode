# 835. Image Overlap
# https://leetcode.com/problems/image-overlap/
import itertools
from msilib import RadioButtonGroup
import time
from typing import List


class Solution:

    def sumOverlap(self, img1: List[List[int]], img2: List[List[int]], n, offsetX=0, offsetY=0) -> int:
        res = 0
        iStart, iFinish = 0, n - offsetX
        if offsetX < 0:
            iStart, iFinish = -offsetX, n

        jStart, jFinish = 0, n - offsetY
        if offsetY < 0:
            jStart, jFinish = -offsetY, n

        for i in range(iStart, iFinish):
            for j in range(jStart, jFinish):
                if img1[i][j] and img2[i+offsetX][j+offsetY]:
                    res += 1
        return res

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        maxSum = 0
        for offsetX in range(-n, n):
            for offsetY in range(-n, n):
                curSum = self.sumOverlap(img1, img2, n, offsetX, offsetY)
                maxSum = max(maxSum, curSum)
        return maxSum


start = time.time()

sol = Solution()

print(sol.largestOverlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))  # 3
print(sol.largestOverlap(img1=[[1]], img2=[[1]]))  # 1
print(sol.largestOverlap(img1=[[0]], img2=[[0]]))  # 0
print(sol.largestOverlap([[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]))  # 1




print("time = ", time.time() - start)
