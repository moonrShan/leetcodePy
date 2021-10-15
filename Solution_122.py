class Solution_122:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        result = 0
        for price in prices:
            if not stack:
                stack.append(price)
            elif price > stack[-1]:
                stack.append(price)
            else:
                result += stack[-1] - stack[0]
                stack = [price]
        result += stack[-1] - stack[0]
        return result
