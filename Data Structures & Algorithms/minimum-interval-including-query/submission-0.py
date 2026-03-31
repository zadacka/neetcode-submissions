

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        for query in queries:
            min_length = math.inf
            for start, stop in intervals:
                if start <= query <= stop:
                    length = 1 + stop - start
                    min_length = min(min_length, length)
            if min_length == math.inf:
                result.append(-1)
            else:
                result.append(min_length)
        return result