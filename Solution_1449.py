class Solution_1449:
    def largestNumber(self, cost, target):
        dp = [0] + [-1] * (target)
        for t in range(1, target + 1):
            for i,c in enumerate(cost):
                if t >= c:
                    dp[t] = max(dp[t],dp[t-c] * 10 + i + 1)
        return str(max(dp[target],0))