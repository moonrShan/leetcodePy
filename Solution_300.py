from typing import List


class Solution_300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        results = []
        result = 1
        for i, num in enumerate(nums):
            candidate = 1
            for j in range(i,-1,-1):
                if num > nums[j]:
                    candidate = max(results[j] + 1, candidate)
            results.append(candidate)
            result = max(result, candidate)
        return result