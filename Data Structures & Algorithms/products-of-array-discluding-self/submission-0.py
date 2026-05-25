class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProduct = 1
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            rightProduct *= nums[i-1]
            output[i] *= rightProduct
        
        leftProduct = 1

        for j in range(len(nums) - 2, -1, -1):
            leftProduct *= nums[j+1]
            output[j] *= leftProduct
        
        return output
        