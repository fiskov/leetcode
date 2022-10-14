# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
from typing import Optional

# test on leetcode only!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        over10 = 0

        res_head = ListNode(0)
        res = res_head

        while l1 or l2 or (over10 > 0):
            digit = over10
            over10 = 0

            if (l1):
                digit += l1.val
                l1 = l1.next

            if (l2):
                digit += l2.val
                l2 = l2.next

            if digit >= 10:
                over10 = 1
                digit -= 10

            res.next = ListNode(digit)
            res = res.next

        return res_head.next

