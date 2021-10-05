class Solution_70:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        prev1, prev2 = 2, 1
        for i in range(n - 2):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
