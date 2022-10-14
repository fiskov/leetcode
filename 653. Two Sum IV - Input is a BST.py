# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import Optional
import TreeNode

null = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findSum(self, root: Optional[TreeNode.TreeNode], k: int) -> bool:
        if root:
            if (k - root.val) in self.bfr:
                return True
            else:
                self.bfr.add(root.val)
                if root.right:
                    if self.findSum(root.right, k):
                        return True
                if root.left:
                    if self.findSum(root.left, k):
                        return True
        return False

    def findTarget(self, root: Optional[TreeNode.TreeNode], k: int) -> bool:
        self.bfr = set()
        return self.findSum(root, k)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

sol = Solution()

root = TreeNode.deserialize("[5,3,6,2,4,null,7]")
print(sol.findTarget(root, 9))  # return True
print(sol.findTarget(root, 28))  # return False

root = TreeNode.deserialize("[1]")
print(sol.findTarget(root, 2))  # return False
