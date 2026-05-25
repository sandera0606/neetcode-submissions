class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(len(nums)):
            curSum = nums[i]
            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
            maxSum = max(maxSum, curSum)
        
        return maxSum