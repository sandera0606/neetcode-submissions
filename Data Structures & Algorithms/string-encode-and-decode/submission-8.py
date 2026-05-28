class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + 'a' + s
        return res

    def decode(self, s: str) -> list[str]:
        l, r = 0, 1
        ans = []
        while l < len(s):
            while s[r] != 'a':
                r += 1
            length = int(s[l:r])
            ans.append(s[r+1:r+1+length])
            l = r + 1 + length
            r = l + 1
        return ans