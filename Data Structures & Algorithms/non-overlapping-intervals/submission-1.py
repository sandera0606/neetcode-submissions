class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0

        prevStart, prevEnd = intervals[0]

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]

            # remove the interval
            if curStart < prevEnd:
                count += 1
                prevEnd = min(prevEnd, curEnd)
            else:
                prevStart, prevEnd = curStart, curEnd
    
        return count