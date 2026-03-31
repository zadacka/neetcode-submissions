class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = max(prices)
        lowest_price_yet = []
        for p in prices:
            lowest_price = min(p, lowest_price)
            lowest_price_yet.append(lowest_price)

        max_profit = 0
        for price, lowest_buy in zip(prices, lowest_price_yet):
            max_profit = max(max_profit, price - lowest_buy)
        
        return max_profit