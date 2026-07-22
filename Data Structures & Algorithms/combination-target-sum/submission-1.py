class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        dp[0] = [[]]

        for num in nums:
            for i in range(num, target + 1):
                old = dp[i-num]
                newLst = []
                for j in range(len(old)):
                    dp[i].append(old[j].copy() + [num])
        return dp[-1]