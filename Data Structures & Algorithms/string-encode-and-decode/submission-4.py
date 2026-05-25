class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "a" + s

        return result

    def decode(self, s: str) -> list[str]:
        i = 0
        result = []

        while i < len(s):
            pointer = i
            while s[pointer] != "a":
                pointer += 1
            length = int(s[i:pointer])
            result.append(s[pointer + 1: pointer + 1 + length])
            i = length + pointer + 1
        
        return result