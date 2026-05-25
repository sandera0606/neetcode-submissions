class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        matching = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for i in range(len(s)):
            cur = s[i]
            if cur == '[' or cur == '(' or cur == '{':
                brackets.insert(0, cur)
            elif len(brackets) != 0:
                recent = brackets.pop(0)
                if matching[cur] != recent:
                    return False
            else:
                return False
        
        return len(brackets) == 0