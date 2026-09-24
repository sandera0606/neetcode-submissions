class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        counts = {}
        res = 1
        l = 0

        for r in range(len(s)):
            letter = s[r]
            if letter in counts:
                counts[letter] += 1
                while counts[letter] > 1:
                    counts[s[l]] -= 1
                    l += 1
            else:
                counts[letter] = 1
            res = max(res, r - l + 1)
            r += 1
        return res