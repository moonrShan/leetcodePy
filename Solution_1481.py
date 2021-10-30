class Solution_1481:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = [v for k, v in counter.items()]
        heapq.heapify(heap)
        while heap:
            if k < heap[0]:
                return len(heap)
            count = heapq.heappop(heap)
            k -= count
        return 0
