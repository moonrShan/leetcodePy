class Solution_992:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums, k):
        counter = collections.Counter()
        distinctCount = 0
        left = 0
        result = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            if counter[nums[right]] == 1:
                distinctCount += 1
            while distinctCount > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    distinctCount -= 1
                left += 1
            result += right - left
        return result
