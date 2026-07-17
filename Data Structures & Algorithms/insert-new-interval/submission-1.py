class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # just merge all the way from the smallest to the largest???
        ans = []

        smaller = newInterval[0]
        larger = newInterval[1]
        next = []

        i = 0
        # first, add all intervals that are outside of the range of the smaller
        while i < len(intervals) and newInterval[0] >= intervals[i][0]:
            ans.append(intervals[i])
            i += 1

        intervals.insert(i, newInterval)
        # then, iterate through the remaining intervals, 
        # updating the new interval if the end value is >= current interval's start interval

        while i < len(intervals):
            if len(ans)==0:
                ans.append(intervals[i])
            elif ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                break
            i += 1

        # append any remaining intervals to the output list
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans