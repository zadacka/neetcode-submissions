class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)  # sort on start
        result = [intervals[0]]
        for interval in intervals[1:]:
            start, end = interval
            previous_start, previous_end = result[-1]
            
            # no overlap
            if start >= previous_end:
                result.append(interval)
            # overlap where the new interval finishes sooner (discard the previous one)
            elif end < previous_end:
                result[-1] = interval
            # overlap where the previous interval finishes sooner (discard the new one)
            else:
                pass
        return len(intervals) - len(result)