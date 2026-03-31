class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = max(prices)
        max_profit = 0
        for p in prices:
            lowest_price = min(p, lowest_price)
            max_profit = max(max_profit, p - lowest_price)
        return max_profit