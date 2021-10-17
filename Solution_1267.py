class Solution_1267:
    def countServers(self, grid: List[List[int]]) -> int:
        connectedRow = collections.defaultdict(int)
        connectedColumn = collections.defaultdict(int)
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    connectedRow[i] += 1
                    connectedColumn[j] += 1
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (connectedRow[i] > 1 or connectedColumn[j] > 1):
                    result += 1
        return result