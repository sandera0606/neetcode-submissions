class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         a = set(nums)
         return (not len(a) == len(nums))