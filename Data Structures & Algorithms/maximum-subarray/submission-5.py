class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # each array item gets the current sum
        minSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i] - minSum, nums[i])
            minSum = min(minSum, nums[i])
        # find the maximum difference between sums
        return maxSum