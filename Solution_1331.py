from typing import List


class Solution_1331:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for num in sorted(arr):
            if num not in rank.keys():
                rank[num] = len(rank) + 1
        result = arr
        for i, num in enumerate(result):
            result[i] = rank[num]
        return result