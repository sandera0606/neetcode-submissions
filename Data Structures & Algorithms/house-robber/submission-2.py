class Solution:
    def rob(self, nums: List[int]) -> int:
        # val(i+2) = val(i) + nums[i+2]
        # val(i+1) = val(i-1) + nums[i+1]
        # u must either rob first or second house, and u must either rob last or second last house.
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        
        ans = [0] * (length + 1)
        ans[length-1] = nums[length-1]
        ans[length-2] = nums[length-2]

        for i in range(length-3, -1, -1):
            ans[i] = nums[i] + max(ans[i+2], ans[i+3])
        
        return max(ans[0], ans[1])