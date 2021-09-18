class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums,n = sorted(nums), len(nums)
        result = 0
        for i in range(n):
            result += nums[i] * (2**i - 1) % (10**9 + 7)
            result -= nums[i] * (2**(n-1-i) - 1) % (10**9 + 7)
        return int(result) % (10**9 + 7)