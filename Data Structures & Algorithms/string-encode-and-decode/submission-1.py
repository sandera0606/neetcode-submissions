class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "é"

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            if s[i] == "é":
                result.append(s[0:i])
                s = s[i+1:]
                i = 0
            else:
                i += 1
        return result

