import collections
import heapq
from typing import List


class Solution_1135:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        G = collections.defaultdict(list)
        for city1, city2, cost in connections:
            G[city1].append((cost, city2))
            G[city2].append((cost, city1))
        queue = [(0, n)]
        visited = set()
        total = 0
        while queue and len(visited) < n:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for edge_cost, next_city in G[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return total if len(visited) == n else -1

