class Solution_115:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1];
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1];
        return dp[m][n]

