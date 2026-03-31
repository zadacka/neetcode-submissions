"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings_brute(self, intervals: List[Interval]) -> bool:
        seen = []
        for interval in intervals:
            for s in seen:
                if s.start <= interval.start < s.end:
                    return False
            seen.append(interval)
        return True
    
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        for i1, i2 in zip(intervals, intervals[1:]):
            if i1.end > i2.start:
                return False
        return True