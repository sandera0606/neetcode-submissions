class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for word in wordDict:
                lenWord = len(word)
                if i - lenWord < 0 or dp[i]:
                    continue
                if s[i-lenWord:i] == word:
                    dp[i] = dp[i-lenWord]
        return dp[-1]