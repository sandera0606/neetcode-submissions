class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0

        if len(nums) < 3:
            return []

        while i < len(nums) - 2 and nums[i] <= 0:
            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        
            target = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j<k:
                result = nums[j] + nums[k] + target
                if result == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                if result > 0:
                    k -= 1
                if result < 0:
                    j += 1
            i += 1

        return ans