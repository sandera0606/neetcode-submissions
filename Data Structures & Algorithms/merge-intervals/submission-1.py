class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        curStart, curEnd = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if curEnd < start:
                merged.append([curStart, curEnd])
                curStart, curEnd = start, end
            else:
                curEnd = max(curEnd, end)
        merged.append([curStart, curEnd])

        return merged