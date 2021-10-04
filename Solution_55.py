class Solutio_55:
    def canJump(self, nums: List[int]) -> bool:
        jumpResults = [False] * len(nums)
        jumpResults[0] = True
        for i,num in enumerate(nums):
            if not jumpResults[i]:
                return False
            for j in range(1,min(num+1, len(nums) - i)):
                jumpResults[i + j] = True
        return True