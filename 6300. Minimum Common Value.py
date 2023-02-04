# 6300. Minimum Common Value
# https://leetcode.com/contest/biweekly-contest-96/problems/minimum-common-value/

import itertools
import time
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]
            if a == b:
                return a
            if a < b:
                i += 1
            else:
                j += 1
            
        return -1


def test(arg1, arg2, arg3):
    res = sol.getCommon(arg1, arg2)
    if res == arg3:
        print("OK", res, "==", arg3)
    else:
        print("--", res, "==", arg3, " <= ", arg1)



start = time.time()

sol = Solution()

test( [1,2,3],  [7], -1)
test( [1,2,3],  [2,4], 2)
test(  [1,2,3,6],  [2,3,4,5], 2)

print("time = ", time.time() - start)
