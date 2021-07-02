class Solution_89:
    def grayCode(self, n: int) -> List[int]:
        if (n == 1): return [0, 1]
        nextResult = self.grayCode(n - 1)
        nextResult0 = [i * 2 for i in nextResult]
        nextResult1 = [i * 2 + 1 for i in nextResult]

        return nextResult0 + nextResult1[::-1]
