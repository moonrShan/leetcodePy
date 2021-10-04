class Solution_1492:
    def kthFactor(self, n: int, k: int) -> int:
        for factor in range(1, n + 1):
            if n % factor == 0:
                k -= 1
                if k == 0:
                    return factor
        return -1
