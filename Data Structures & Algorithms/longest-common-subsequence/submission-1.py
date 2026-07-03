class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # make a matrix
        # number is length of current common subsequence
        dp = [[0] * len(text1) for i in range(len(text2))]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    if i > 0 and j > 0:
                        val = dp[i-1][j-1]
                    else:
                        val = 0
                    dp[i][j] = 1 + val
                else:
                    val = 0
                    if i > 0:
                        val = max(val, dp[i-1][j])
                    if j > 0:
                        val = max(val, dp[i][j-1])
                    dp[i][j] = val
        return dp[len(text2)-1][len(text1)-1]