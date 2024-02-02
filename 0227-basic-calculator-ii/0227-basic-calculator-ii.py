class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'
        
        for i, char in enumerate(s):
            # Is a number
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            # Is add, sub, multi, or div
            if char in '+-*/' or i == len(s)-1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack[-1] = stack[-1] * current_number
                elif operation == '/':
                    stack[-1] = int(stack[-1] / current_number)
                operation = char
                current_number = 0
            # print(stack)
        return sum(stack)
        