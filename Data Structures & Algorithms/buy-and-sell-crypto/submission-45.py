class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price_so_far = prices[0]
        for price_today in prices:
            profit = price_today - lowest_price_so_far
            max_profit = max(max_profit, profit)
            lowest_price_so_far = min(lowest_price_so_far, price_today)
        return max_profit