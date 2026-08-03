class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if to - nums[i] - i <= 0:
                to = i
        return to == 0