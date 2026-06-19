class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0

        while i < len(nums) - 1 and nums[i] <= 0:
            target = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if target + nums[j] + nums[k] < 0:
                    j += 1
                elif target + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
            i += 1
            while i < len(nums) - 1 and nums[i] == nums[i-1]:
                i += 1
        return ans