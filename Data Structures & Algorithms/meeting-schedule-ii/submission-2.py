"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = [(i.start, True) for i in intervals] + [(i.end, False) for i in intervals]
        times = sorted(times)  # tuple sorting puts False before True in tie breaks
        count, max_count = 0, 0

        for (time, start) in times:
            count = (count + 1) if start else (count - 1)
            max_count = max(max_count, count)
        return max_count