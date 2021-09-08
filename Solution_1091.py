import collections
from typing import List


class Solution_1091:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        visited = set((0, 0))
        queue = collections.deque([(0, 0, 1)])
        while queue:
            i, j, dis = queue.popleft()
            if i == n - 1 and j == n - 1: return dis
            for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
                x = i + d1
                y = j + d2
                if 0 <= x <= n - 1 and 0 <= y <= n - 1 and grid[x][y] == 0 and (x, y) not in visited:
                    queue.append((x, y, dis + 1))
                    visited.add((x, y))
        return -1
