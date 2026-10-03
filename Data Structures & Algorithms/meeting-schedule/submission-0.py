"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2: return True
        intervals.sort(key=lambda x: x.start)

        old = intervals[0]
        for inter in intervals[1:]:
            # print(inter.start, old.end)
            if inter.start < old.end:
                return False
            old = inter
        return True