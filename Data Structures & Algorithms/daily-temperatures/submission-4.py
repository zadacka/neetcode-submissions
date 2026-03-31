class Solution:
    def dailyTemperatures_n2(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, temperature in enumerate(temperatures):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperature:
                    result.append(j - i)
                    break
            else:
                result.append(0)
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        
        stack = []  # pairs of (t, i)

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                t, i = stack.pop()
                result[i] = idx - i
            stack.append((temperature, idx))
        
        return result
