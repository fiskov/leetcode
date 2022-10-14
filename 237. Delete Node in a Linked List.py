# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val) + ", " + str(self.next)


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


h1 = ListNode(4)
h2 = ListNode(5)
h3 = ListNode(1)
h4 = ListNode(9)
h1.next = h2
h2.next = h3
h3.next = h4

sol = Solution()

print(h1)
sol.deleteNode(h2)
print(h1)
