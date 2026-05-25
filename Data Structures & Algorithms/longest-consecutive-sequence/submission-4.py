class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mySet = set(nums)
        longest = 0

        for num in mySet:
            if not num-1 in mySet:
                i = 0
                while num + i in mySet:
                    i += 1
                longest = max(longest, i)
        
        return longest