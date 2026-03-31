class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        for interval in intervals:
            start, end = interval
            if result:
                previous_start, previous_end = result[-1]
                if previous_start <= start <= previous_end:
                    result[-1] = [previous_start, max(previous_end, end)]
                else:
                    result.append(interval)
            else:
                result.append(interval)
        return result