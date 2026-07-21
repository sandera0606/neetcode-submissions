"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        started, ended = 0, 0
        res = 0

        i, j = 0, 0

        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                started += 1
                i += 1
            else:
                ended += 1
                j += 1
            res = max(res, started - ended)

        return res