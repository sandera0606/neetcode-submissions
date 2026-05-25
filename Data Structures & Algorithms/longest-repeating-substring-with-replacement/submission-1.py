from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = Counter()
        max_freq = 0
        l = 0
        longest = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            max_freq = max(max_freq, chars[s[r]])

            if (r - l + 1) - max_freq > k:
                chars[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest



            

            
            