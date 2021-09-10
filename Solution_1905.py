from typing import List


class Solution_1905:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        result = 0
        for i in range(m):
            for j in range(n):
                validIland = False
                if grid2[i][j] == 1:
                    validIland = self.dfs(i, j, grid1, grid2)
                result += validIland
        return result

    def dfs(self, i: int, j: int, grid1: List[List[int]], grid2: List[List[int]]) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(grid2)
        n = len(grid2[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0: return True
        grid2[i][j] = 0
        result = grid1[i][j] == 1
        for x, y in directions:
            result &= self.dfs(i + x, y + j, grid1, grid2)

        return result
