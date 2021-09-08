from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution_95:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        results = []
        for i in range(1, n + 1):
            root = TreeNode(i)
            leftList = self.generateSubTrees(1, i)
            rightList = self.generateSubTrees(i + 1, n + 1)
            for left in leftList:
                root.left = left
                for right in rightList:
                    root.right = right
                    results.append(root)
        return results

    def generateSubTrees(self, Min, Max):
        if (Min == Max): return [None]
        results = []
        for i in range(Min, Max):
            root = TreeNode(i)
            leftList = self.generateSubTrees(Min, i)
            rightList = self.generateSubTrees(i + 1, Max)
            for left in leftList:
                root.left = left
                for right in rightList:
                    root.right = right
                    results.append(root)
        return results

def main():
    testObject = Solution_95()
    print(testObject.generateTrees(3))

if __name__=="__main__":
    main()