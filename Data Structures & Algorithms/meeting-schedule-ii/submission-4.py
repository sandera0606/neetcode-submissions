"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 1:
            return len(intervals)
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()

        count = 0
        cur = 0

        si = 0
        ei = 0

        while si < len(starts):
            if starts[si] < ends[ei]:
                cur += 1
                si += 1
                count = max(count, cur)
            else:
                cur -= 1
                ei += 1

        return count