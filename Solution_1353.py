from _ast import List
from heapq import heappush, heappop


class Solution_1353:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        count = 0
        i, n = 0, len(events)
        d = 0
        while i < n or pq:
            if not pq:
                d = events[i][0]
            while i < n and d >= events[i][0]:
                heappush(pq, events[i][1])
                i += 1
            heappop(pq)
            count += 1
            d += 1
            while pq and pq[0] < d:
                heappop(pq)

        return count