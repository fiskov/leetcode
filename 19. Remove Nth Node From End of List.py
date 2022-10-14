# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # add to ListNode class expansion for testing
    def __repr__(self):
        return str(self.val) + ", " + str(self.next)
        # return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # signle node in list
        if not head.next:
            return None

        # skip N nodes
        p1 = head
        for _ in range(n):
            p1 = p1.next

        # n = length of nodes
        if not p1:
            return head.next

        # move until the End of nodes
        p2 = head
        while p1.next:
            p2 = p2.next
            p1 = p1.next

        # remove Node
        p3 = p2
        p3 = p3.next
        p2.next = p3.next
        return head


sol = Solution()
h1 = list_to_LL([1,2,3,4,5])
print(sol.removeNthFromEnd(head = h1, n = 2))
h1 = list_to_LL([1])
print(sol.removeNthFromEnd(head = h1, n = 1))
h1 = list_to_LL([1,2])
print(sol.removeNthFromEnd(head = h1, n = 1))
h1 = list_to_LL([1,2])
print(sol.removeNthFromEnd(head = h1, n = 2))
