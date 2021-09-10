from typing import List


class Solution_718:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
        return max(map(max,dp))