class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval

        result = []
        for idx, interval in enumerate(intervals):
            start, end = interval

            # 1) new interval is completely before this
            if new_end < start:
                result.append(newInterval)
                return result + intervals[idx:]
            # 2) new interval is completely after this
            elif end < new_start:
                result.append(interval)
            # 3) new interval overlaps with this
            else:
                newInterval = [min(start, new_start), max(end, new_end)]  # key bit - update newInterval but NOT result (yet)
                new_start, new_end = newInterval
        # if we got here, the new interval was at the end
        result.append(newInterval)
        return result