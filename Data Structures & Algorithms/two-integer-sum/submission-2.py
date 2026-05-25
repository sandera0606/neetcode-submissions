class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = dict()
        for i in range(len(nums)-1):
            elements[nums[i]] = i
            search = target - nums[i+1]
            if search in elements:
                return [elements.get(search), i+1]
