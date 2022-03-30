from typing import List


class Solution_78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            rest = self.subsets(nums[1:])
            return [[nums[0]] + r for r in rest] + rest