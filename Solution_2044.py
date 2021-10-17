from typing import List


class Solution_2044:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for num in nums:
            maximum |= num
        dp = collections.defaultdict(int)
        dp[0] = 1
        for num in nums:
            items = list(dp.items())
            for k,v in items:
                dp[num | k] += v
        return dp[maximum]