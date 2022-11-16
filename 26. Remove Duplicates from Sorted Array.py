# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import time
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 1, 0
        while i < len(nums):
            if nums[i] == nums[k]:
                i += 1
            else:
                k += 1
                if k != i:
                    nums[k] = nums[i]

        return k+1


def test(arg1, arg2):
    res = sol.removeDuplicates(arg1)
    if len(arg1) < 20:
        if res == arg2:
            print("OK", res, "==", arg2)
        else:
            print("--", res, "==", arg2, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

sol = Solution()
nums = [1,1,2]
test(nums, 2)
print(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
test(nums, 5)
print(nums)

print("time = ", time.time() - start)
