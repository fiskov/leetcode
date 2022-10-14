# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
from typing import Optional
from xml.dom.minicompat import NodeList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val) + ", " + str(self.next)


def list_to_LL(arr):
    if len(arr) < 1:
        return None
    node = ListNode(arr[0])
    node.next = list_to_LL(arr[1:])
    return node


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head0 = ListNode(0)
        head0.next = head
        node1 = head0
        node2 = head0.next
        while node2.next:
            if node2.next:
                node1 = node1.next
                node2 = node2.next
            if node2.next:
                node2 = node2.next
        node1.next = node1.next.next
        return head0.next


def test(bfr):
    h1 = list_to_LL(bfr)
    print(h1)
    sol = Solution()
    sol.deleteMiddle(h1)
    print(h1)

test([1,2,3,4,5])
test([1,2])
test([1])

