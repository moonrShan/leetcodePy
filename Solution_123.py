class Solution_123:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        buy2 = float('inf')
        sell1 = 0
        sell2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2
