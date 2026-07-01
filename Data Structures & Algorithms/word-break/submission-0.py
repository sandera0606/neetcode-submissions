class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        strLen = len(s)
        
        dp = [False] * strLen

        for i in range(strLen):
            for word in wordDict:
                wordLen = len(word)
                if i + 1 - wordLen >= 0 and (i + 1 - wordLen == 0 or dp[i - wordLen]) and s[i + 1 - wordLen : i + 1] == word:
                    dp[i] = True

        return dp[-1]