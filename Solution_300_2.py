class Solution_300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [0] * len(nums)
        size = 0
        for x in nums:
            i = 0
            j = size
            while i < j:
                m = (i+j) // 2
                if tail[m] < x:
                    i = m + 1
                else:
                    j = m
            tail[i] = x
            size = max(size,i + 1)
        return size