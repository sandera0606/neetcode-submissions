from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = defaultdict(int)

        l = 0
        maxFreq = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            maxFreq = max(maxFreq, counts[s[r]])
                
            while r - l - k - maxFreq + 1> 0:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            
        return longest


            

            
            