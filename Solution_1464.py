class Solution_1464:
    def maxProduct(self, nums: List[int]) -> int:
        m = n = float('-inf')
        for num in nums:
            if num >= m:
                n = m
                m = num
            elif num > n:
                n = num
        return (m - 1) * (n - 1)