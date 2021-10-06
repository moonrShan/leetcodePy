class Solution_654_2:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            n = TreeNode(num)
            while stack and num > stack[-1].val:
                n.left = stack.pop()

            if stack:
                stack[-1].right = n
            stack.append(n)

        return stack[0]