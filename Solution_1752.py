class Solution_1752:
    def check(self, nums: List[int]) -> bool:
        rotation = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if rotation:
                    return False
                rotation = True
        if rotation:
            return nums[0] >= nums[-1]
        return True
