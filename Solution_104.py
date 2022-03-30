from collections import deque
from typing import Optional

from Solution_102 import TreeNode


class Solution_104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([[root,1]])
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append([node.left,depth+1])
            if node.right:
                queue.append([node.right,depth+1])
        return depth