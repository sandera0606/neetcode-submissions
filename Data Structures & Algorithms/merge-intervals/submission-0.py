class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        intervals.sort()

        # merge the intervals
        start, end = intervals[0]
        ans = []

        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                ans.append((start, end))
                start, end = intervals[i]
            else:
                end = max(end, intervals[i][1])
        
        ans.append((start, end))
        return ans
            