class Solution_1987:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        dp = [0, 0]
        for c in binary:
            dp[int(c)] = (sum(dp) + int(c)) % mod
        return (sum(dp) + ('0' in binary)) % mod