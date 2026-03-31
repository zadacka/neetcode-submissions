"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        seen = []
        for interval in intervals:
            for s in seen:
                if s.start <= interval.start < s.end:
                    return False
            seen.append(interval)
        return True
            