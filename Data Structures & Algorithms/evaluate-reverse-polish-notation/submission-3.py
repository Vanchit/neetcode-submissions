class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in {'+','-','*','/'}:
                stack.append(int(c))
                continue
            second = stack.pop()
            first = stack.pop()

            if c == '+':
                result = first + second 
            elif c == '*':
                result = first * second
            elif c == '-':
                result = first - second
            else:
                result = abs(first) // abs(second)

                if (first < 0) != (second < 0):
                    result = -result
            
            stack.append(result)
        return stack[-1]