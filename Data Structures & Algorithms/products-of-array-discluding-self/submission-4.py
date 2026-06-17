class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            ans[i] = prod
            prod *= nums[i]
        
        leftProd = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= leftProd
            leftProd *= nums[i]
            
        return ans