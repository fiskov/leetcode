# 1323. Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

import time
from typing import List, Optional


class Solution:
    def maximum69Number(self, num: int) -> int:
        d = divmod(num, 1000)
        if d[0] == 6:
            return num+3000
        d = divmod(d[1], 100)
        if d[0] == 6:
            return num+300
        d = divmod(d[1], 10)
        if d[0] == 6:
            return num+30
        if d[1] == 6:
            return num+3
        return num


def test(arg1, arg2):
    res = sol.maximum69Number(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test(9669, 9969)
test(9996, 9999)
test(9999, 9999)
test(99, 99)

print("time = ", time.time() - start)
