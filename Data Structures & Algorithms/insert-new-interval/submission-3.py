class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        cur = 0

        while cur < len(intervals) and intervals[cur][1] < newInterval[0]:
            ans.append(intervals[cur])
            cur += 1
        if cur == len(intervals):
            ans.append(newInterval)
            return ans

        # insert new interval
        curStart = min(newInterval[0], intervals[cur][0])
        curEnd = newInterval[1]

        while cur < len(intervals) and intervals[cur][0] <= curEnd:
            curEnd = max(curEnd, intervals[cur][1])
            cur += 1
        
        ans.append([curStart, curEnd])

        while cur < len(intervals):
            ans.append(intervals[cur])
            cur += 1
        
        return ans