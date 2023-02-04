# 6275. Minimum Operations to Make Array Equal II
# https://leetcode.com/contest/biweekly-contest-96/problems/minimum-operations-to-make-array-equal-ii/

import itertools
import time
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        s1, s2, sm = 0, 0, 0

        if nums1 == nums2:
            return 0
        if k == 0:
            return -1

        for i in range(len(nums1)):
            a = nums1[i]
            b = nums2[i]
            d = abs(a-b)
            if d and d<k:
                return -1

            s1 += a
            s2 += b
            sm += d

        if s1 != s2 or sm % (k*2) != 0:
            return -1

        return sm // (k*2)


def test(nums1, nums2, k, r):
    res = sol.minOperations(nums1, nums2, k)
    if res == r:
        print("OK", res, "==", r)
    else:
        print("--", res, "==", r, " <= ", nums1)


start = time.time()

sol = Solution()

test(nums1=[4, 3, 1, 4], nums2=[1, 3, 7, 1], k=3, r=2)

test(nums1=[3, 8, 5, 2], nums2=[2, 4, 1, 6], k=1, r=-1)

test(nums1=[4, 3, 1, 4], nums2=[2, 3, 6, 1], k=10, r=-1)
test(nums1=[2, 2, 2, 2], nums2=[3, 1, 2, 2], k=4, r=-1)
test(nums1=[2, 5], nums2=[5, 2], k=2, r=-1)
test(nums1=[10,5,15,20], nums2=[20,10,15,5], k=0, r=-1)

print("time = ", time.time() - start)