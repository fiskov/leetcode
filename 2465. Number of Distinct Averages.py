# 2465. Number of Distinct Averages
# https://leetcode.com/contest/biweekly-contest-91/problems/number-of-distinct-averages/

from collections import defaultdict
import time
from typing import List, Counter


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        c = Counter()
        for i in range(len(nums) // 2):
            value = (nums[i]+nums[len(nums)-i-1])
            c[value] += 1
        return len(set(c))


def test(arg1, arg2):
    res = sol.distinctAverages(arg1)
    if len(arg1) < 10:
        if res == arg2:
            print("OK", res, "==", arg2)
        else:
            print("--", res, "==", arg2, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

sol = Solution()

test([4,1,4,0,3,5], 2)
test([1,100], 1)

print("time = ", time.time() - start)
