class Solution_42:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        temp = 0
        for right, value in enumerate(height):
            left = right
            while stack and height[stack[-1]] < value:
                left = stack.pop()
                temp += height[left]
            if not stack:
                result += (right - left) * height[left] - temp
                temp = 0
            stack.append(right)

        for i in range(len(stack) - 1):
            result += height[stack[i + 1]] * (stack[i + 1] - stack[i] - 1)

        return result - temp
