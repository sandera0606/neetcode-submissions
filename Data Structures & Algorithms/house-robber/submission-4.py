class Solution:
    def rob(self, nums: List[int]) -> int:
        # either rob last house or second last house
        if len(nums) <= 2:
            return max(nums)
        nums[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])