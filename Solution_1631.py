import collections
import heapq
from typing import List


class Solution_1631:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        dist = collections.defaultdict(lambda: float('inf'))
        minHeap = [(0,0,0)]
        DIR = [[0,1],[0,-1],[1,0],[-1,0]]
        while minHeap:
            d,i,j = heapq.heappop(minHeap)
            if i == m - 1 and j == n-1:
                return d
            for (x,y) in DIR:
                ni,nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n:
                    newDist = max(d,abs(heights[ni][nj] - heights[i][j]))
                    if dist[(ni,nj)] > newDist:
                        dist[(ni,nj)] = newDist
                        heapq.heappush(minHeap,(dist[(ni,nj)],ni,nj))


                        