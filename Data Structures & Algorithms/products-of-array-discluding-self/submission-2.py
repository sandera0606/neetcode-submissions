class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # without extra arrays
        ans = [1] * len(nums)
        rightProd = 1
        for i in range(len(nums)):
            ans[i] = rightProd
            rightProd *= nums[i]
        
        leftProd = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= leftProd
            leftProd *= nums[i]
        return ans
