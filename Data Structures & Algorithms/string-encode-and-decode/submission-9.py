class Solution:
    delimiter = 'a'

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            length = len(s)
            ans += str(length) + self.delimiter + s
        return ans

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        ans = []

        while l < len(s):
            while s[r] != self.delimiter:
                r += 1
            length = int(s[l:r])
            ans.append(s[r+1:r+length+1])
            l = r + length + 1
            r = l
        
        return ans