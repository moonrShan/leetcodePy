import heapq
from typing import List
class Solution_253:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        result = 0
        for interval in sorted(intervals):
            while h and h[0] <= interval[0]:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
            result = max(result, len(h))
        return result

