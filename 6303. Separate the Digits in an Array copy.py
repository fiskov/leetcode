# 6303. Separate the Digits in an Array
# https://leetcode.com/contest/biweekly-contest-97/problems/separate-the-digits-in-an-array

import itertools
import time
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            for x in str(n):
                res.append(int(x))
        return res


def test(arg1, arg2):
    res = sol.separateDigits(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)



start = time.time()

sol = Solution()

test( [13,25,83,77], [1,3,2,5,8,3,7,7])
test( [7,1,3,9], [7,1,3,9])

print("time = ", time.time() - start)
