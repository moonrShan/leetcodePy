class Solution_1922:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        if n == 2: return 20
        return 20 * self.countGoodNumbers(n - 2) % (10 ** 9 + 7)
