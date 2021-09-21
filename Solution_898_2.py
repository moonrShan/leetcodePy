class Solution_898_2:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, cur = set(), set()
        for num in arr:
            cur = {num | j for j in cur} | {num}
            res |= cur
        return len(res)