class Solution_162:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = len(nums)
        p = (left + right) // 2
        while left <= p < right:
            if (p == 0 or nums[p] > nums[p - 1]) and (p == n - 1 or nums[p] > nums[p + 1]):
                return p
            if p != n - 1 and nums[p] < nums[p + 1]:
                left = p + 1
                p = (left + right) // 2
                continue
            if p != 0 and nums[p] < nums[p - 1]:
                right = p
                p = (left + right) // 2
                continue

        return p