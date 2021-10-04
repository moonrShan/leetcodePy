class Solution_343:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        if n % 3 == 2:
            return 3 ** (n // 3) * 2
        return 3 ** (n // 3)