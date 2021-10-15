class Solution_121:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        previousMin = float('inf')
        for price in prices:
            result = max(result, price - previousMin)
            previousMin = min(previousMin,price)
        return result