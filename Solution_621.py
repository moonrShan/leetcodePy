import heapq
from collections import Counter

class Solution_621:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        time = 0
        while heap:
            i = 0
            temp = []
            while i <= n:
                if heap:
                    v, k = heapq.heappop(heap)
                    if -v > 1:
                        temp.append((v + 1, k))
                time += 1
                if not heap and not temp:
                    break
                i += 1
            for l in temp:
                heapq.heappush(heap, l)

        return time