class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        ans = 0

        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]: # cur start
                # no overlap
                prevEnd = intervals[i][1]
            else: # overlap
                ans += 1
                prevEnd = min(prevEnd, intervals[i][1])

        return ans