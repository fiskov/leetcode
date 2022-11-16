# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

import time
from typing import List, Optional
from TreeNode import TreeNode, deserialize
null = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return
        res = []
        stack = [(root, "")]
        while stack:
            node, routeString = stack.pop()
            if not node.left and not node.right:
                res.append(routeString + str(node.val))
            else:
                if node.left:
                    stack.append((node.left, routeString + str(node.val) + "->"))
                if node.right:
                    stack.append((node.right, routeString + str(node.val) + "->"))
        return res


def test(arg1, arg2):
    res = sol.binaryTreePaths(deserialize(arg1))
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test("[1,2,3,null,5]", ["1->2->5","1->3"])
test("[1]", ["1"])

print("time = ", time.time() - start)
