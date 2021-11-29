class Solution_53:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArrayEnd = []
        maxSubArrayStart = []
        for i, num in enumerate(nums):
            if i > 0:
                maxSubArrayEnd.append(max(num, num + maxSubArrayEnd[-1]))
            else:
                maxSubArrayEnd.append(num)

        for i, num in list(enumerate(nums))[::-1]:
            if i < len(nums) - 1:
                maxSubArrayStart.append(max(num, num + maxSubArrayStart[-1]))
            else:
                maxSubArrayStart.append(num)

        result = float('-inf')
        for i in range(len(nums)):
            result = max(result, maxSubArrayStart[len(nums) - 1 - i] + maxSubArrayEnd[i] - nums[i])

        return result