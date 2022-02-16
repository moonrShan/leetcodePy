from typing import List


class Solution_849:
    def maxDistToClosest(self, seats: List[int]) -> int:
        pos = []
        for i,x in enumerate(seats):
            if x : pos.append(i)
        result = max(pos[0],len(seats) - pos[-1] - 1)
        for i in range(len(pos) - 1):
            candidate = pos[i+1] - pos[i]
            result = max(result, candidate // 2)
        return result