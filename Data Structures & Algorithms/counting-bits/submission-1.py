class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        cur = 1

        for i in range(1, n+1):
            if i == cur:
                dp[i] = 1
                cur *= 2
            else:
                prevInd = (int) (i-cur/2)
                dp[i] = dp[prevInd] + 1
                print(cur)
        return dp