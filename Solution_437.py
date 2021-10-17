# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution_437:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            result += self.pathSumFromRoot(node, targetSum)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

    def pathSumFromRoot(self, root, target):
        if not root: return 0
        result = 0
        if root.val == target:
            result += 1
        if root.left:
            result += self.pathSumFromRoot(root.left, target - root.val)
        if root.right:
            result += self.pathSumFromRoot(root.right, target - root.val)
        return result