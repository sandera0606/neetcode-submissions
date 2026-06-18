class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in nums:
            if not num - 1 in unique:
                length = 0
                while num in unique:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest