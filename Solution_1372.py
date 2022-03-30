# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Solution_102 import TreeNode


class Solution_1372:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = 0
        _, lr = self.zigzag(root.left)
        rl, _ = self.zigzag(root.right)
        self.res = max(lr + 1, rl + 1, self.res)
        return self.res

    def zigzag(self, root):
        if not root: return [-1, -1]
        _, lr = self.zigzag(root.left)
        rl, _ = self.zigzag(root.right)
        self.res = max(lr + 1, rl + 1, self.res)
        return [lr + 1, rl + 1]