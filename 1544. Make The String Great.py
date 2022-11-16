# 1544. Make The String Great
# https://leetcode.com/problems/make-the-string-great/

import itertools
import time
from typing import List, Optional
import functools


class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for a in s:
            if len(res) and res[-1] == a.swapcase():
                res.pop()
            else:
                res.append(a)

        return "".join(res)


def test(arg1, arg2):
    res = sol.makeGood(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test("leEeetcode", "leetcode")
test("abBAcC", "")
test("s", "s")
test("kkdsFuqUfSDKK", "kkdsFuqUfSDKK")

print("time = ", time.time() - start)
