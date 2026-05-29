class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        leftProd = 1
        for i in range(len(nums)):
            ans[i] *= leftProd
            leftProd *= nums[i]
        
        rightProd = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= rightProd
            rightProd *= nums[j]
        
        return ans