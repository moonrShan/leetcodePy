import heapq
from typing import List

class Solution_1648:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        h = [-x for x in inventory]
        heapq.heapify(h)
        total = 0
        while orders:
            current = heapq.heappop(h)
            orders -= 1
            total -= current
            heapq.heappush(h,current + 1)
        return total % (10**9 + 7)