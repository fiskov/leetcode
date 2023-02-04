# 6263 (2498). Frog Jump II
# https://leetcode.com/contest/biweekly-contest-93/problems/frog-jump-ii/
import itertools
import math
import bisect
import time
from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) < 4:
            return stones[-1]

        maxlen = 0
        s1 = [0] + stones[1:-1:2] + [stones[-1]]
        s2 = [0] + stones[2:-1:2] + [stones[-1]]

        for i in range(len(s1)-1):
            step = abs(s1[i]-s1[i+1])
            maxlen = max(maxlen, step)
        for i in range(len(s2)-1):
            step = abs(s2[i]-s2[i+1])
            maxlen = max(maxlen, step)

        return maxlen


def test(**kwargs):
    if not hasattr(test, "counter"):
        test.counter = 0
    test.counter += 1

    method_list = [func for func in dir(Solution) if callable(
        getattr(Solution, func)) and not func.startswith("__")]
    method = getattr(Solution, method_list[0])

    kwarg_dict = dict(itertools.islice(kwargs.items(), len(kwargs)-1))
    res = method(Solution, **kwarg_dict)

    res0 = list(kwargs.items())[-1][1]
    msg = "OK" if res == res0 else "--"
    print(f"{test.counter:3}: {msg} {res0} == {res}")


start = time.time()

sol = Solution()

test(stones = [0,2,5,6,7], output=5)
test(stones = [0,3,9], output=9)

print("time = ", time.time() - start)
