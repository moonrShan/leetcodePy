# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Solution_102 import TreeNode


class Solution_1382:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        result = []
        self.dfs(root,result)
        median = len(result) // 2
        root = TreeNode(result[median])
        root.left = self.constructTree(result[:median])
        root.right = self.constructTree(result[median+1:])
        return root

    def dfs(self, root, result):
        if not root: return None
        self.dfs(root.left,result)
        result.append(root.val)
        self.dfs(root.right,result)

    def constructTree(self,result):
        if not result : return None
        median = len(result) // 2
        root = TreeNode(result[median])
        root.left = self.constructTree(result[:median])
        root.right = self.constructTree(result[median+1:])
        return root