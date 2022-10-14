# 2404. Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num % 2 == 0:
                if num in m:
                    m[num] += 1
                else:
                    m[num] = 1

        if len(m) == 0:
            return -1

        max_value = max(m.values())

        m2 = {key for key, value in m.items() if value == max_value}

        return min(m2)


sol = Solution()

# print(sol.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]))
# print(sol.mostFrequentEven(nums=[4, 4, 4, 9, 2, 4]))
# print(sol.mostFrequentEven(nums=[29, 47, 21, 41, 13, 37, 25, 7]))
print(sol.mostFrequentEven(
    nums=[8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))
