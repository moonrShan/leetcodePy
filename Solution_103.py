# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

from Solution_102 import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        result = []
        level = 0
        while queue:
            tempResult = []
            for i in range(len(queue)):
                node = queue.popleft()
                tempResult.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2:
                result.append(tempResult[::-1])
            else:
                result.append(tempResult)
            level += 1
        return result