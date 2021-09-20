class Solution_1922_2:
    def countGoodNumbers(self, n: int) -> int:
        mask = 10 ** 9 + 7
        if n %  2 == 1:
            return 20 ** (n // 2) * 5 % mask
        return 20 ** (n // 2) % mask