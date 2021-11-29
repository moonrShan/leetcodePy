class Solution_2089:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        countSmaller = 0
        countTarget = 0
        for num in nums:
            if num < target:
                countSmaller += 1
            if num == target:
                countTarget += 1
        return [i + countSmaller for i in range(countTarget)]