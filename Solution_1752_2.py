class Solution_1752:
    def check(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                if flag: return False
                flag = True
        return True