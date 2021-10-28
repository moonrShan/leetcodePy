class Solution_1337:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            strength = (-sum(row), -i)
            if len(heap) < k:
                heapq.heappush(heap, strength)
            elif strength > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, strength)
        result = []
        while heap:
            result.append(-heapq.heappop(heap)[1])
        return result[::-1]
