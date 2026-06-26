class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            m = (l + r) // 2
            minimum = min(minimum, nums[m])
            if nums[m] >= nums[l] and nums[r] < nums[l]:
                l = m + 1
            elif nums[m] >= nums[l]:
                r = m - 1
            elif nums[m] <= nums[l]:
                r = m - 1
    
        return minimum