class Solution_2064:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total = sum(quantities)
        left = total // n
        if total % n :
            left += 1
        right = total + 1
        while left < right:
            mid, need = (left + right) // 2, 0
            for q in quantities:
                need += q // mid
                if q % mid:
                    need += 1
            if need > n:
                left = mid + 1
            else:
                right = mid
        return left