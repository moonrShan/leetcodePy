from typing import Optional

from Solution_102 import TreeNode


class Solution_872:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1 = [root1];
        s2 = [root2]
        while s1 and s2:
            if self.dfs(s1) != self.dfs(s2):
                return False
        return not s1 and not s2

    def dfs(self, stack):
        while True:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                return node.val
