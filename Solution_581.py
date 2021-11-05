class Solution_581:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        index_1 = self.func_1(nums)
        index_2 = self.func_2(nums)
        ans = index_2 - index_1 + 1
        return ans if ans > 0 else 0

    def func_1(self, nums):
        stack = []
        index = len(nums) + 1
        for i, n in enumerate(nums):
            while stack and n < stack[-1][1]:
                indx, value = stack.pop()
                index = min(indx, index)
            stack.append((i, n))
        return index

    def func_2(self, nums):
        stack = []
        index = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > stack[-1][1]:
                indx, value = stack.pop()
                index = max(indx, index)
            stack.append((i, nums[i]))
        return index