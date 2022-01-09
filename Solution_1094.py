import collections
from typing import List


class Solution_1094:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        addPassenger = collections.defaultdict(int)
        dropPassenger = collections.defaultdict(int)
        start = float('inf')
        end = float('-inf')
        for trip in trips:
            addPassenger[trip[1]] += trip[0]
            dropPassenger[trip[2]] += trip[0]
            start = min(start,trip[1])
            end = max(end,trip[2])
        currentCapacity = 0
        for i in range(start,end+1):
            currentCapacity += addPassenger[i]
            currentCapacity -= dropPassenger[i]
            if currentCapacity > capacity:
                return False
        return True