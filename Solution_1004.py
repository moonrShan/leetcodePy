class Solution_1004:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #not me
        left = 0
        cntZeros = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cntZeros += 1
            while cntZeros > k:  # Case nums[left, right] contains more than k zeros, move `left` util the subarray has no more than k zeros
                if nums[left] == 0: cntZeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans