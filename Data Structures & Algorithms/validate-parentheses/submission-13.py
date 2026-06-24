class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')':'(', '}':'{',']':'['}
        stack = []

        for char in s:
            if char in matches.keys():
                if not stack or matches[char] != stack[-1]:
                    return False
                stack.pop()
            elif char in matches.values():
                stack.append(char)
            else:
                return False
        return stack == []