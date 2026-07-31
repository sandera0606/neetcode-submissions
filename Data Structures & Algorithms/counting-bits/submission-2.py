class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        if n < 1:
            return dp
        dp[1] = 1

        cur = 1

        for i in range(2, n+1):
            if i == cur * 2:
                dp[i] = 1
                cur *= 2
            else:
                dp[i] = dp[i-cur] + 1
                print(cur)
        return dp