# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
import itertools
import math
import bisect
import time
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


def test(**kwargs):
    if not hasattr(test, "counter"):
        test.counter = 0

    method_list = [func for func in dir(Solution) if callable(
        getattr(Solution, func)) and not func.startswith("__")]
    method = getattr(Solution, method_list[0])

    kwarg_dict = dict(itertools.islice(kwargs.items(), len(kwargs)-1))
    res = method(Solution, **kwarg_dict)

    res0 = list(kwargs.items())[-1][1]
    msg = "OK" if res == res0 else "--"
    print(msg, res0, "==", res)


start = time.time()

sol = Solution()

test(nums=[1, 3, 5, 6], target=5, output=2)
test(nums=[1, 3, 5, 6], target=2, output=1)
test(nums=[1, 3, 5, 6], target=7, output=4)

print("time = ", time.time() - start)
