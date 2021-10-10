class Solution_63:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]