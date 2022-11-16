# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

import itertools
import time
from typing import List, Optional


class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        # bit-mask 001, 010, 100
        masks = [1 << i for i in range(len(nums))]
        # combinations 0, 1, 10, 100, 101, 110, 111
        for cmbn in range(1, 2**len(nums)):
            xor = 0
            # look in "mask"
            for i, mask in enumerate(masks):
                # if mask and combination
                if mask & cmbn:
                    # function
                    xor ^= nums[i]
            res += xor
        return res

    def subsetXORSum0(self, nums: List[int]) -> int:
        res = 0
        for L in range(len(nums) + 1):
            res += sum([functools.reduce(operator.xor, subset, 0) for subset in itertools.combinations(nums, L)])

        return res


def test(arg1, arg2):
    res = sol.subsetXORSum(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test([1,3], 6)
test([5,1,6], 28)
test([3,4,5,6,7,8], 480)

print("time = ", time.time() - start)
