class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        ansLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if ansLen < r - l - 1:
                ansLen = r - l - 1
                longest = s[l+1:r]    

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if ansLen < r - l - 1:
                ansLen = r - l - 1
                longest = s[l+1:r]
        return longest