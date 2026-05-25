class Solution:

    def is_castable(s):
        try:
            int(s)
            return True
        except (ValueError, TypeError):
            return False

    def encode(self, strs: list[str]) -> str:
        ans = ""
        for s in strs:
            length = len(s)
            ans += str(length) + 'a'
            ans += s
        return ans

    def decode(self, s: str) -> list[str]:
        intBegin = 0
        intEnd = 0
        ans = []
        totLen = len(s)
        while intBegin < totLen:
            while(Solution.is_castable(s[intBegin : intEnd + 1])):
                intEnd += 1 # haha intend
            length = int(s[intBegin : intEnd])
            nextBegin = intEnd + 1 + length
            ans.append(s[intEnd + 1:nextBegin])
            intBegin = nextBegin
            intEnd = intBegin
        return ans