"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def sort_by_start(interval):
            return interval.start
        intervals = sorted(intervals, key=sort_by_start)
        previous = Interval(start=-1, end=0)
        for interval in intervals:
            if interval.start < previous.end or interval.end < previous.end:
                return False
            previous = interval
        return True
