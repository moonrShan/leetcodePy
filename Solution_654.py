class Solution_654:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return
        maxNum, maxIndex = float('-inf'), -1
        for i, num in enumerate(nums):
            if maxNum < num:
                maxNum = num
                maxIndex = i

        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])

        return root