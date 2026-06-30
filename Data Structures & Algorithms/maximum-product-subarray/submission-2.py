class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, num, curMin * num)
            curMin = min(curMin * num, tmp, num)
            res = max(res, curMax)

        return res