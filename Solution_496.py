class Solution_496:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        nextGreaterDict = {}
        for num in nums2:
            while stack and stack[-1] < num:
                nextGreaterDict[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            if num not in nextGreaterDict:
                result.append(-1)
            else:
                result.append(nextGreaterDict[num])

        return result