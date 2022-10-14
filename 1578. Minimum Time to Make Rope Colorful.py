# 1578. Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# leet_1578
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        n = len(colors)
        colors += '!'  # additional end-symbol
        sum_total = 0
        while i < n:
            cnt = 0
            sum = 0
            max = 0
            # start of consecutive balloons
            if colors[i] == colors[i+1]:
                cnt = 1
                sum = neededTime[i]
                max = neededTime[i]
                i += 1
                while colors[i-1] == colors[i] and i < n:
                    cnt += 1
                    sum += neededTime[i]
                    if max < neededTime[i]:
                        max = neededTime[i]
                    i += 1
            # leave only max element
            if cnt:
                sum_total += sum - max
            else:
                i += 1

        return sum_total


sol = Solution()

print(sol.minCost(colors = "abaac", neededTime = [1,2,3,4,5]))  # 3
print(sol.minCost(colors = "abc", neededTime = [1,2,3]))  # 0
print(sol.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))  # 2
