# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# leet_113
from typing import List, Optional
from binarytree import Node, build

null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:            
        self.bigList = []
        self.curList = []

    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def pathSum(self, root: Optional[Node], targetSum: int) -> List[List[int]]:
        if root:
            self.curList.append(root.val)
            targetSum -= root.val
            # check leaf
            if not root.left and not root.right:
                # targetSum is ok
                if targetSum == 0:
                    self.bigList.append(self.curList.copy())
            else:       
                # not leaf and go deeper
                self.pathSum(root.left, targetSum)
                self.pathSum(root.right, targetSum)
            targetSum += root.val
            self.curList.pop()
        return self.bigList


sol = Solution()

#nodes = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
binary_tree = build([-2,null,-3])
print(binary_tree)
print(sol.pathSum(root=binary_tree, targetSum=-5))
#print(sol.pathSum(root=[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum=22))
#print(sol.pathSum(root=[1, 2, 3], targetSum=5))
