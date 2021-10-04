class Solution_463:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return self.dfs(i, j, grid, visited)

    def dfs(self, x, y, grid, visited):
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1 or not grid[x][y]:
            return 1
        result = 0
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if (x + dx, y + dy) not in visited:
                visited.add((x, y))
                result += self.dfs(x + dx, y + dy, grid, visited)
        return result