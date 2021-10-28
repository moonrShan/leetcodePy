class Solution_1046:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            rest = abs(first - second)
            if rest:
                heapq.heappush(heap,-rest)
        return -heap[0] if heap else 0