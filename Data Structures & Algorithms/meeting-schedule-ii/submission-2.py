"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [interval.start for interval in intervals], [interval.end for interval in intervals]
        starts.sort()
        ends.sort()

        cur = 0
        res = 0
        startInd, endInd = 0, 0
        while startInd < len(intervals):
            if starts[startInd] < ends[endInd]:
                cur += 1
                res = max(cur, res)
                startInd +=1
            else:
                cur -= 1
                endInd += 1


        return res