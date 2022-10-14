# 334. Increasing Triplet Subsequence
# 976. Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

from typing import List


class Solution:
    def getPerimeter(self, a, b, c) -> int:
        if a+b > c and a+c > b and b+c > a:
            return a+b+c

    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-2):
            res = self.getPerimeter(nums[i], nums[i+1], nums[i+2])
            if res:
                return res
        return 0


sol = Solution()

print(sol.largestPerimeter(nums = [2,1,2]))    # 5
print(sol.largestPerimeter(nums = [1,2,3,4,5,6,7,8,9,10]))    # 27
print(sol.largestPerimeter(nums = [1,2,1]))    # 0
