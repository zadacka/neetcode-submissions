class Solution:
    def dailyTemperatures_alex(self, temperatures: List[int]) -> List[int]:
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


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # idx, temp
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx, stack_temp = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append((idx,  temp))
        return result