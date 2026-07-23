class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # all of the intervals before newInterval
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # merge intervals that match
        # we already know that intervals[i][1] >= newInterval[0]
        # ends after it starts
        if i >= len(intervals):
            return res + [newInterval]

        start, end = min(intervals[i][0], newInterval[0]), min(intervals[i][1], newInterval[1])
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            end = max(intervals[i][1], newInterval[1])
            i += 1
        res.append([start, end])

        # add all remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res