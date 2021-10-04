class Solution_55_2:
    def canJump(self, nums: List[int]) -> bool:
        maxReachPosition = 0
        for i,num in enumerate(nums):
            if i > maxReachPosition:
                return False
            maxReachPosition = max(maxReachPosition, i + num)
        return True