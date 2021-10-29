class Solution_1985:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,int(num))
            elif int(num) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,int(num))
        return str(heap[0])