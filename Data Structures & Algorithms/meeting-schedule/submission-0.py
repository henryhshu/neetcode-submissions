"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        curr = 0
        for i in intervals:
            start = i.start
            end = i.end
            if start < curr:
                return False
            curr = end
        return True