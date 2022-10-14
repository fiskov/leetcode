# 
# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        if not list1 and not list2:
            return None

        head = tail = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        # add reminder
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return head.next


sol = Solution()


list1 = list_to_LL([5])
list2 = list_to_LL([1,2,4])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([2,4,6])
list2 = list_to_LL([1,3,5])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([1,3,5])
list2 = list_to_LL([2,4,6])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([1,2,4])
list2 = list_to_LL([1,3,4])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([])
list2 = list_to_LL([])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([])
list2 = list_to_LL([0])
print(sol.mergeTwoLists(list1, list2))

list1 = list_to_LL([2])
list2 = list_to_LL([1])
print(sol.mergeTwoLists(list1, list2))

