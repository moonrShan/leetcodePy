from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    resultDict = {}  # key:(min,max), value: combination

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        results = []
        for i in range(1, n + 1):
            leftList = self.generateSubTrees(1, i)
            rightList = self.generateSubTrees(i + 1, n + 1)
            for left in leftList:
                for right in rightList:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    results.append(root)
        return results

    def generateSubTrees(self, Min, Max):
        if (Min == Max): return [None]
        if (((Min, Max)) in self.resultDict):
            return self.resultDict[(Min, Max)]
        results = []
        for i in range(Min, Max):
            leftList = self.generateSubTrees(Min, i)
            rightList = self.generateSubTrees(i + 1, Max)
            for left in leftList:
                for right in rightList:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    results.append(root)
        self.resultDict[(Min, Max)] = results
        return results