class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            second = stack.pop()
            first = stack.pop()

            if token == "+":
                result = first + second

            elif token == "-":
                result = first - second

            elif token == "*":
                result = first * second

            else:
                # Division must truncate toward zero
                result = abs(first) // abs(second)

                if (first < 0) != (second < 0):
                    result = -result

            stack.append(result)

        return stack[-1]