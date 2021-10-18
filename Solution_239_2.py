class Solution_239_2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        output.append(-heap[0][0])
        for i in range(1, len(nums) - k + 1):
            end = i + k - 1
            heapq.heappush(heap, (-nums[end], end))
            while (heap[0][1] < i):
                heapq.heappop(heap)

            output.append(-heap[0][0])
        return output