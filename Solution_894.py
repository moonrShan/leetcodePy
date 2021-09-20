# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution_894:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            ans = []
            for leftCount in range(n):
                rightCount = n - 1 - leftCount
                for left in self.allPossibleFBT(leftCount):
                    for right in self.allPossibleFBT(rightCount):
                        mid = TreeNode(0)
                        mid.left = left
                        mid.right = right
                        ans.append(mid)
            self.memo[n] = ans
        return self.memo[n]