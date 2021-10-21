class Solution:
    def __init__(self):
        self.memo = {}

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if tuple(arr) in self.memo: return self.memo[tuple(arr)]
        if len(arr) == 1: return 0
        total = float('inf')
        for i in range(1, len(arr)):
            left = arr[:i]
            right = arr[i:]
            currentRoot = max(left) * max(right)
            leftVal = self.mctFromLeafValues(left)
            rightVal = self.mctFromLeafValues(right)
            total = min(total, leftVal + rightVal + currentRoot)
        self.memo[tuple(arr)] = total
        return total