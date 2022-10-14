# 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/
from typing import List, Optional
# from binarytree import Node, build

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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root:
            if depth == 1:
                node = TreeNode(val=val, left=root)
                return node
            elif depth == 2:
                node_left = TreeNode(val=val, left=root.left)
                node_right = TreeNode(val=val, right=root.right)
                root.left = node_left
                root.right = node_right
            else:
                self.addOneRow(root=root.left, val=val, depth=depth-1)
                self.addOneRow(root=root.right, val=val, depth=depth-1)
        return root
