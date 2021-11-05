class Solution_441:
    def arrangeCoins(self, n: int) -> int:
        left = 0; right = n + 1
        while left < right:
            mid = (left + right) // 2
            cost = (mid + 1) * mid // 2
            if cost == n:
                return mid
            elif cost < n:
                left = mid + 1
            else:
                right = mid
        return left - 1