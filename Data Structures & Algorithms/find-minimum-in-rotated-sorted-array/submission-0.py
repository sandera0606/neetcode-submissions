class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        minimum = min(nums[l], nums[r])

        while l <= r:
            m = r + l // 2
            minimum = min(minimum, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] <= nums[r]:
                r = m - 1

        return minimum


