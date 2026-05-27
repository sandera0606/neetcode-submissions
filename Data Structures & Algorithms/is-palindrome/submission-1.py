class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        l = 0
        r = len(cleaned) - 1

        while(l<r):
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True