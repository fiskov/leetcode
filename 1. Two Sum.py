# 1. Two Sum
# https://leetcode.com/problems/two-sum/
from typing import List, Optional

# test on leetcode only!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numbers = {}
        for i, number in enumerate(nums):
            remain = target - number
            if remain in previous_numbers:  # hash-table has remain-value => get index of it
                return [previous_numbers[remain], i] 
            else:
                previous_numbers[number] = i    # add to hash-table value:index

        return []

