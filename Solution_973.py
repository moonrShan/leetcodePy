from typing import List


class Solution_973:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [[x*x+y*y, x, y] for x,y in points]
        heapq.heapify(h)
        result = []
        for i in range(k):
            d,x,y = heapq.heappop(h)
            result.append([x,y])
        return result