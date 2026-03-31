class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        lowest_price = prices[0]
        for price in prices:
            profit = price - lowest_price
            best_profit = max(best_profit, profit)
            lowest_price = min(lowest_price, price)
        return best_profit