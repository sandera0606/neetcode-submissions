class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        longest = 0

        l, r = 0, 0

        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            r += 1
            longest = max(longest, r - l)
        
        return longest

        