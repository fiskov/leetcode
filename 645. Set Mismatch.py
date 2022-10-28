# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        a = [0] * (n+1)
        missed, twiced = 0, 0
        for c in nums:
            if a[c]:
                twiced = c
            a[c] += 1

        for i in range(n+1):
            if a[i] == 0:
                missed = i

        return [twiced, missed]

sol = Solution()

print(sol.findErrorNums([1,2,2,4]))  # 2,3
print(sol.findErrorNums([1,1]))     # 1,2
print(sol.findErrorNums([2,2]))     # 2,1
print(sol.findErrorNums([3,2,2]))   # 2,1
