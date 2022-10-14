# 112. Path Sum
# https://leetcode.com/problems/path-sum/
from typing import List, Optional
from binarytree import Node, build

null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if not root.left and not root.right and targetSum == root.val:
                return True

            if self.hasPathSum(root.left, targetSum-root.val) or \
               self.hasPathSum(root.right, targetSum-root.val):
                return True
        return False


sol = Solution()

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
binary_tree = build([5,4,8,11,null,13,4,7,2,null,null,null,null,null,1])
# print(binary_tree)
print(sol.hasPathSum(root=binary_tree, targetSum = 22))  # true
binary_tree = build([1,2,3])
print(sol.hasPathSum(root=binary_tree, targetSum = 5))  # false
binary_tree = build([])
print(sol.hasPathSum(root=binary_tree, targetSum = 0))  # false
binary_tree = build([1,2])
print(sol.hasPathSum(root=binary_tree, targetSum = 1))  # false
