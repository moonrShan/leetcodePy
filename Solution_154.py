from typing import List
class Solution_154:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right -left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid if nums[right] != nums[mid] else right - 1
        return nums[left]