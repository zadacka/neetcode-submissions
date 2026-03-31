class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, temperature in enumerate(temperatures):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperature:
                    result.append(j - i)
                    break
            else:
                result.append(0)
        return result
