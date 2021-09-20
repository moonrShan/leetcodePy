import collections


class Solution_1823:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque([i for i in range(1,n+1)])
        while len(queue) > 1:
            for i in range(1,k+1):
                skip = queue.popleft()
                if i != k:
                    queue.append(skip)
        return queue.popleft()