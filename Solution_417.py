class Solution_417:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            self.dfs(heights, i, 0, p_visited, m, n)
            self.dfs(heights, i, n - 1, a_visited, m, n)
        for j in range(n):
            self.dfs(heights, 0, j, p_visited, m, n)
            self.dfs(heights, m - 1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, heights, i, j, visited, m, n):
        visited[i][j] = True
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or heights[x][y] < heights[i][j]:
                continue
            self.dfs(heights, x, y, visited, m, n)