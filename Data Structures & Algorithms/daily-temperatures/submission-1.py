class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        # Start from the final day and move backwards
        for current in range(n - 1, -1, -1):

            # Remove days that are colder than or equal to the current day
            while (
                stack
                and temperatures[current] >= temperatures[stack[-1]]
            ):
                stack.pop()

            # The top index is now the next warmer day
            if stack:
                result[current] = stack[-1] - current

            # Store the current day's index
            stack.append(current)

        return result