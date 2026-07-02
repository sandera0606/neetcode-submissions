class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        one = 1 # ways to i - 2
        two = 1 if s[1] == '0' or int(s[0:2]) > 26 else 2  # ways up to i-1
        
        if s[1] == '0' and int(s[0:2]) > 26:
            return 0

        for i in range(2, len(s)):
            if s[i] == '0' and (s[i-1] == '0' or int(s[i-1:i+1])>26):
                return 0
            elif s[i] == '0': # 10 or 20:
                new = one
            elif s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                new = two
            else:
                new = one + two
            one = two
            two = new
        
        return two