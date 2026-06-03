from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26 # kep track of each letters' occurrences
        maxLetter = 0
        ans = 0
        l = 0
        maxLetter = 0

        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] += 1

            maxLetter = maxLetter if counts[ord(s[r])-ord('A')] <= counts[ord(s[maxLetter])-ord('A')] else r
            maxFreq = counts[ord(s[maxLetter]) - ord('A')]

            while (r - l + 1) - maxFreq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


            

            
            