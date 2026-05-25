from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        numUnique = 0
        counter = [0] * 26 # letters of the alphabet
        res = 0
        maxFreq = 0
        l = 0
        for r in range(0, len(s)):
            charIndex = ord(s[r]) - ord('A')
            counter[charIndex] += 1
            maxFreq = max(maxFreq, counter[charIndex])
            while r - l + 1 - maxFreq > k:
                lChar = ord(s[l]) - ord('A')
                counter[lChar] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res


            

            
            