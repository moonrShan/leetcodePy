class Solution_27:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentPos = 0
        for num in nums:
            if num == val:
                continue
            nums[currentPos] = num
            currentPos += 1
        return currentPos