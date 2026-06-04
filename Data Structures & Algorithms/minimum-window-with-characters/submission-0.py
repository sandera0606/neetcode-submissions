class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tChars = [0] * 26 * 2
        # lowercase = ord(char) - ord('a')
        # uppercase = ord(char) - ord('A') + 26
        sChars = [0] * 26 * 2

        if len(t) > len(s):
            return ""

        l, r = 0, 0
        shortestLen = len(s)
        shortest = ""

        for char in t:
            if char.isupper():
                tChars[ord(char) - ord('A') + 26] += 1
            else:
                tChars[ord(char) - ord('a')] += 1

        while r < len(s):
            # move r up until it has a substring
            # move l up until it doesn't have a substring
            cur = s[r]
            if cur.isupper():
                sChars[ord(cur) - ord('A') + 26] += 1
            else:
                sChars[ord(cur) - ord('a')] += 1
            
            while self.isSubstring(sChars, tChars):
                if shortestLen > r - l:
                    shortest = s[l:r+1]
                    shortestLen = r - l + 1
                if s[l].isupper():
                    sChars[ord(s[l]) - ord('A') + 26] -= 1
                else:
                    sChars[ord(s[l]) - ord('a')] -= 1
                l += 1
            
            r += 1


        return shortest
    
    def isSubstring(self, sDict, tDict):
        for i in range(len(sDict)):
            if tDict[i] > sDict[i]:
                return False
        return True