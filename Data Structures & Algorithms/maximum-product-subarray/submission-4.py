class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]
        res = maxProd

        for i in range(1, len(nums)):
            cur = nums[i]
            oldMinProd = minProd
            minProd = min(minProd * cur, cur, maxProd * cur)
            maxProd = max(oldMinProd * cur, cur, maxProd * cur)
            res = max(maxProd, res)
        return res