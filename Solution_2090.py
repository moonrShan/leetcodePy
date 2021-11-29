class Solution_2090:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        totalSum = 0
        result = [-1] * len(nums)
        for i, num in enumerate(nums):
            totalSum += num
            if i == 2 * k:
                result[i - k] = totalSum // (2 * k + 1)
            if i > 2 * k:
                totalSum -= nums[i - 2 * k - 1]
                result[i - k] = totalSum // (2 * k + 1)
        return result
