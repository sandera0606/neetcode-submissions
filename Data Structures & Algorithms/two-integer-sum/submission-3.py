class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = dict() # key = desired = target - nums[index], value = index
        for i in range(len(nums)):
            val = nums[i]
            if val in myDict.keys():
                return [myDict[val], i]
            desired = target - val
            myDict[desired] = i
        return None
