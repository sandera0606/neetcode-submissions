class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prevMax = curMax
            prevMin = curMin

            curMax = max(num, prevMax * num, prevMin * num)
            curMin = min(num, prevMax * num, prevMin * num)

            res = max(res, curMax)
    
        return res