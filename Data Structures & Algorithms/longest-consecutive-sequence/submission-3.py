class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestseq = 0
        myset = set(nums)
        
        for num in nums:
            if not num-1 in myset:
                curseq = 1
                while num + curseq in myset:
                    curseq += 1
                
                longestseq = max(longestseq, curseq)

        return longestseq