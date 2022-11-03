# 2453. Destroy Sequential Targets
# https://leetcode.com/problems/destroy-sequential-targets/
from bisect import bisect
from collections import Counter, defaultdict
import time
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d = {}
        max_k = 0
        max_cnt = 0

        for i in nums:
            k = i % space
            if k in d:
                d[k][0] = min(d[k][0], i)
                d[k][1] += 1
            else:
                d[k] = [i, 1]

        for t in d.values():
            if max_cnt < t[1]:
                max_cnt = t[1]
                max_k = t[0]
            elif max_cnt == t[1]:
                max_k = min(t[0], max_k)

        return max_k


def test(arg1, arg2, arg3):
    res = sol.destroyTargets(arg1, arg2)
    if res == arg3:
        print("OK", res, "==", arg3)
    else:
        print("--", res, "==", arg3, " <= ", arg1)


start = time.time()

sol = Solution()

test([1,5,5,2,5,3,1,2,4,5], 4, 1)
test([3,7,8,1,1,5], 2, 1)
test([1,3,5,2,4,6], 2, 1)
test([6,2,5], 100, 2)
test([372,683], 10000, 372)
test([1,5,3,2,2], 10000, 2)
test([625879766,235326233,250224393,501422042,683823101,948619719,680305710,733191937,182186779,353350082], 4, 235326233)

print("time = ", time.time() - start)
