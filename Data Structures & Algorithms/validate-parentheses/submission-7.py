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
                brackets.insert(0, bracket)
            elif len(brackets) != 0:
                recent = brackets.pop(0)
                if matching[bracket] != recent:
                    return False
            else:
                return False
        
        return len(brackets) == 0