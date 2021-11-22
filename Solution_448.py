class Solution_448:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num) - 1
            nums[num] = -abs(nums[num])
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result
