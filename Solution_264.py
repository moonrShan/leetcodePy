import heapq


class Solution_264:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        while n:
            value = heapq.heappop(heap)
            while heap and value == heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,value*2)
            heapq.heappush(heap,value*3)
            heapq.heappush(heap,value*5)
            n -= 1
        return value