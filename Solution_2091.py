class Solution_2091:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimumValue = float('inf'); minimumIndex = -1
        maximumlValue = float('-inf'); maximumIndex = -1
        for i, num in enumerate(nums):
            if num < minimumValue:
                minimumValue = num
                minimumIndex = i
            if num > maximumlValue:
                maximumlValue = num
                maximumIndex = i
        miniLeft = minimumIndex + 1; miniRight = len(nums) -  minimumIndex
        maxLeft = maximumIndex + 1; maxRight = len(nums) - maximumIndex
        return min([max(miniLeft,maxLeft),max(miniRight,maxRight),miniLeft+maxRight,miniRight+maxLeft])