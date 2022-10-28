# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

import bisect
import re
from typing import List


class Solution:
    # simple, but success 91ms 97.4%, 14.2MB 67.5%
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m and n:
            if nums1[-1] < nums2[0]:
                x = nums1 + nums2
            elif nums2[-1] < nums1[0]:
                x = nums2 + nums1
            else:
                x = sorted(nums1 + nums2)
        elif m:
            x = nums1
        else:
            x = nums2

        n = divmod(len(x), 2)
        if n[1]:
            return x[n[0]]
        else:
            return (x[n[0] - 1] + x[n[0]]) / 2



    # bisect, 275ms 5%, 14.2MB 67.5%
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        for c in nums2:
            bisect.insort(nums1, c)
        n = len(nums1)
        n2 = n // 2
        if n % 2:
            return nums1[n2]
        else:
            return (nums1[n2 - 1] + nums1[n2]) / 2


sol = Solution()

print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))    # 2.0
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))  # 2.5
print(sol.findMedianSortedArrays(nums1 = [3,4], nums2 = [1,2]))  # 2.5
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4]))  # 2.5
print(sol.findMedianSortedArrays(nums1 = [1,3,5], nums2 = [2,4]))  # 3
print(sol.findMedianSortedArrays(nums1 = [0,0], nums2 = [0,0]))  # 0
print("----")
print(sol.findMedianSortedArrays(nums1 = [0,0,0,0], nums2 = [-1,0,0,0,0,0,1]))  # 0
print(sol.findMedianSortedArrays(nums1 = [0,0,0,0,0], nums2 = [-1,0,0,0,0,0,1]))  # 0
print(sol.findMedianSortedArrays(nums2 = [0,0,0,0,0], nums1 = [-1,0,0,0,0,0,1]))  # 0
print("----")
print(sol.findMedianSortedArrays(nums1 = [1], nums2 = [2,3,4]))    # 2.5
print(sol.findMedianSortedArrays(nums1 = [1], nums2 = [2,3]))    # 2.0
print(sol.findMedianSortedArrays(nums1 = [1], nums2 = [2]))    # 1.5
print("----")
print(sol.findMedianSortedArrays(nums1 = [2], nums2 = [1,3,4]))    # 2.5
print(sol.findMedianSortedArrays(nums1 = [2], nums2 = [1,3,4,5,6,7]))    # 4.0
print(sol.findMedianSortedArrays(nums1 = [4], nums2 = [1,2,3]))    # 2.5
