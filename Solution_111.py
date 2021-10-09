# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Solution_102 import TreeNode


class Solution_111:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        leftDepth,rightDepth = float('inf'), float('inf')
        if root.left:
            leftDepth = self.minDepth(root.left)
        if root.right:
            rightDepth = self.minDepth(root.right)
        return min(leftDepth,rightDepth) + 1