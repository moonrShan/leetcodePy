from typing import List


class Solution_376:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [1] * len(nums)
        down = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if num > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                if num < nums[j]:
                    down[i] = max(down[i], up[j] + 1)

        return max(max(up), max(down))