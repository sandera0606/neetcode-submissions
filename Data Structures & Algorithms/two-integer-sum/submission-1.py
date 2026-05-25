class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            cur = nums[i]
            search = target-cur
            for j in range(i+1, len(nums)):
                if nums[j] == search:
                    return [i, j]
