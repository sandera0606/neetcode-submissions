class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longestseq = 1
        myset = set(nums)
        
        for num in nums:
            if not num-1 in myset:
                curseq = 1
                cur = num + 1
                while cur in myset:
                    curseq += 1
                    cur += 1
                
                longestseq = max(longestseq, curseq)

        return longestseq