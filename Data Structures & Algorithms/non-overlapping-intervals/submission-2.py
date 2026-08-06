class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevStart, prevEnd = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            if prevEnd <= curStart:
                prevStart, prevEnd = curStart, curEnd
            else:
                count += 1
                prevEnd = min(prevEnd, curEnd)
        
        return count