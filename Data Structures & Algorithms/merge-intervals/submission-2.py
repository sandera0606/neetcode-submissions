class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        
        curStart, curEnd = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if curEnd < start: # non-overlapping
                ans.append([curStart, curEnd])
                curStart, curEnd = start, end
                continue
            curEnd = max(curEnd, end)

        ans.append([curStart, curEnd])


        return ans