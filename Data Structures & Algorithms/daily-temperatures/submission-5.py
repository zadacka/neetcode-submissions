class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        future_highs = []
        idx = len(temperatures) - 1
        for temp in reversed(temperatures):
            print(temp, future_highs)
            while future_highs and future_highs[-1][1] <= temp:
                _ = future_highs.pop()
            if future_highs and future_highs[-1][1] > temp:
                result.append(future_highs[-1][0] - idx)
            else:
                result.append(0)
            future_highs.append((idx, temp))
            idx -= 1
        return list(reversed(result))


