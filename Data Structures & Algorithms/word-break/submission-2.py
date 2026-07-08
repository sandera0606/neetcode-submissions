class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                wordLen = len(word)
                if i - wordLen + 1 >= 0:
                    frag = s[i - wordLen + 1 : i + 1]
                    if frag == word:
                        if i - wordLen < 0:
                            res[i] = True
                        else:
                            res[i] = res[i] or res[i-wordLen]

        return res[-1]