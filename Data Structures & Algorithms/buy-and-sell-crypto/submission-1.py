class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        low = prices[0]
        lowest_so_far = []
        for price in prices:
            low = min(low, price)
            lowest_so_far.append(low)

        high = prices[-1]
        highest_after_this = []
        for price in prices[::-1]:
            high = max(high, price)
            highest_after_this.append(high)
        highest_after_this = list(reversed(highest_after_this))
        
        best = 0
        for low, high in zip(lowest_so_far, highest_after_this):
            best = max(best, high - low)
        
        # print(lowest_so_far)
        # print(highest_after_this)
        return best

    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(price, lowest)
            result = max(result, price - lowest)
        return result