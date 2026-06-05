class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '[', '{']
        stack = []
        for char in s:
            if char in open:
                stack.append(char)
            elif len(stack)>0 and self.matches(stack[-1], char):
                stack.pop()
            else:
                return False
        return stack == []
        
    def matches(self, l: char, r: char) -> bool:
        if l == '(':
            return r == ')'
        if l == '[':
            return r == ']'
        if l == '{':
            return r == '}'
        return False