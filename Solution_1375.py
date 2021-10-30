class Solution_1375:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = res = 0
        for i, a in enumerate(light):
            right = max(right, a)
            res += right == i + 1
        return res