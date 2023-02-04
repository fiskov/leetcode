# 27. Remove Element
# https://leetcode.com/problems/remove-element/
import itertools
import math
import bisect
import time
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != j:
                    nums[j] = nums[i]
                j += 1

        return j


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

test(nums = [3,3,3,3], val = 3, output=0)
test(nums = [3,2,2,3], val = 3, output=2)
test(nums = [0,1,2,2,3,0,4,2], val = 2, output=5)

print("time = ", time.time() - start)
