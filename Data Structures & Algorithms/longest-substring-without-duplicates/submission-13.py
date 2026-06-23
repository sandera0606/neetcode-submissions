class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        chars = set()
        l = 0
        for r in range(len(s)):
            char = s[r]
            while char in chars:
                chars.remove(s[l])
                l += 1
            chars.add(char)
            longest = max(r - l + 1, longest)

        return longest
        