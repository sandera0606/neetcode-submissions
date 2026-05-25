class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        matching = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for bracket in s:
            if bracket in matching.values():
                brackets.append(bracket)
            elif brackets:
                recent = brackets.pop()
                if matching[bracket] != recent:
                    return False
            else:
                return False
        
        return len(brackets) == 0