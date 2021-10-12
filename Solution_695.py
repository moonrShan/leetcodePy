class Solution_695:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                result = max(result, self.dfs(grid, i, j))
        return result

    def dfs(self, grid, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        result = 0
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            result += self.dfs(grid, x + dx, y + dy)
        return result + 1