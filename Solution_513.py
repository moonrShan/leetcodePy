# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional

from Solution_102 import TreeNode


class Solution_513:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        while queue:
            candidate = queue[0].val
            for i in range(len(queue)):
                root = queue.popleft()
                if (root.left):
                    queue.append(root.left)
                if (root.right):
                    queue.append(root.right)
            if not queue:
                return candidate