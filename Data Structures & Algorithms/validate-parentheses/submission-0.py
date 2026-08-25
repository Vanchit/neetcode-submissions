class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
        
        
            elif c == '{':
                stack.append('}')
        
        
            elif c == '[':
                stack.append(']')

            elif not stack or stack.pop() != c: #Start with Close braces or closing bracket doesnt match 
                return False

        return len(stack) == 0