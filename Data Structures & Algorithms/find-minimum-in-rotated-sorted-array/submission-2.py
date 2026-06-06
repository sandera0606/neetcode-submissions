class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l < r:
            mid = (l + r) // 2
            res = min(res, nums[mid], nums[l], nums[r])
            if nums[r] > nums[l]:
                if nums[l] < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return res


