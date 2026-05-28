class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            target = nums[i]
            if target > 0:
                break
            if i > 0 and target == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j<k:
                if target + nums[j] + nums[k] < 0:
                    j += 1
                elif target + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        # [-4, -1, -1, 0, 1, 2]
        # target = -1
        # -1 + 2 + 1 > 0
        # 
        return res