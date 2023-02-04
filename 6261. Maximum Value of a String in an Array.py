# 6261. Maximum Value of a String in an Array
# https://leetcode.com/contest/biweekly-contest-93/problems/maximum-value-of-a-string-in-an-array/
import itertools
import math
import bisect
import time
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for str in strs:
            if str.isnumeric():
                res.append(int(str))
            else:
                res.append(len(str))

        return max(res)


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

test(strs = ["alic3","bob","3","4","00000"], output=5)
test(strs = ["1","01","001","0001"], output=1)

print("time = ", time.time() - start)
