class Solution_1730:
    def getFood(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue = deque([(i, j, 0)])
        visited = set(queue[0][:2])
        while queue:
            x, y, step = queue.popleft()
            if grid[x][y] == '#':
                return step
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, +1]]:
                newx, newy = x + dx, y + dy
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] != 'X' and (
                newx, newy) not in visited:
                    queue.append([newx, newy, step + 1])
                    visited.add((newx, newy))
        return -1
