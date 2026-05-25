class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProds = [1] * len(nums)
        leftProds = [1] * len(nums)

        # first pass: do rightProds and leftProds
        for r in range(1, len(nums)):
            l = len(nums) - r
            rightProds[r] = rightProds[r - 1] * nums[r - 1]
            leftProds[l-1] = leftProds[l] * nums[l]

        print(rightProds)
        print(leftProds)
        # 2nd pass: make ans
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] *= rightProds[i] * leftProds[i]
        
        return ans