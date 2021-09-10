from typing import List


class Solution_764:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        grid = [[0] * n for _ in range(n)]
        for i in range(n):
            count = 0
            for j in range(n):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                    grid[i][j] = count

            count = 0
            for j in range(n - 1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                    grid[i][j] = min(grid[i][j], count)

        for j in range(n):
            count = 0
            for i in range(n):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                    grid[i][j] = min(grid[i][j], count)

            count = 0
            for i in range(n - 1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                    grid[i][j] = min(grid[i][j], count)

        return max(map(max, grid))
    #        return max([max(row) for row in grid])