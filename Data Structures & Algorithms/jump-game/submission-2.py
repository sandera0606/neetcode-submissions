class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if to - i - nums[i] <= 0:
                to = i
        return to == 0