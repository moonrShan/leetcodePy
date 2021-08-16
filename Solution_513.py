# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_513:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            candidate = queue[0].val
            for i in range(len(queue)):
                root = queue.pop(0)
                if (root.left):
                    queue.append(root.left)
                if (root.right):
                    queue.append(root.right)
            if not queue:
                return candidate