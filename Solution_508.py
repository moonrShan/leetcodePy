# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.counter = collections.defaultdict(int)
        self.calculateTotal(root)
        result = []
        maximumCount = max(self.counter.values())
        for key in self.counter:
            if self.counter[key] == maximumCount:
                result.append(key)
        return result

    def calculateTotal(self, root):
        if not root: return 0
        leftTotal = self.calculateTotal(root.left)
        rightTotal = self.calculateTotal(root.right)
        total = leftTotal + rightTotal + root.val
        self.counter[total] += 1
        return total