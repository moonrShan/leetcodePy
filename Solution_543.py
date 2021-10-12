# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Solution_814 import TreeNode


class Solution_543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        self.result = max(self.result, leftDepth + rightDepth)
        return self.result

    def depth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        self.result = max(self.result, leftDepth + rightDepth)
        return max(leftDepth, rightDepth) + 1