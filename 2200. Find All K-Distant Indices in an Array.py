# 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        j_last = -1
        for i in range(len(nums)):
            if nums[i] == key:
                start = max(i - k, j_last)
                finish = min(i + k, len(nums) - 1)

                if start == j_last and start < finish:
                    start += 1
                if finish > j_last:
                    for j in range(start, finish + 1):
                        result.append(j)
                        j_last = j
        return result


sol = Solution()

print(sol.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(sol.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2))
