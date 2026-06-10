class Solution:
    def isValid(self, s: str) -> bool:
        matches = {']' : '[', ')' : '(' , '}':'{'}
        stack = []

        for p in s:
            if p in matches.values():
                stack.append(p)
            else:
                if p in matches and stack and matches[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []