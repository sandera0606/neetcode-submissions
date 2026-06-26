class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ans = ""

        for i in range(len(s)):
            l, r, = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > longest:
                ans = s[l+1:r]
                longest = r - l - 1
            l, r, = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if r - l - 1 > longest:
                ans = s[l+1:r]
                longest = r - l - 1
        
        return ans