class Solution_174:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                    continue
                if i + 1 < m and j + 1 < n:
                    dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
                    continue
                if i + 1 < m:
                    dp[i][j] = max(dp[i + 1][j] - dungeon[i][j], 1)
                    continue
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j + 1] - dungeon[i][j], 1)
        return dp[0][0]


