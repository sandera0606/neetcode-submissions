class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num-1 in numSet:
                continue
            cur = 1
            while num+1 in numSet:
                num += 1
                cur += 1
            longest = max(cur, longest)
        return longest