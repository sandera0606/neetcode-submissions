class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_txt = ''.join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(clean_txt) - 1

        while(i < j):
            if clean_txt[i] != clean_txt[j]:
                return False

            i += 1
            j -= 1
        
        return True