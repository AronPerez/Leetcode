class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n  # Initialize the answer array with zeros
        stack = []  # Create an empty stack to keep track of people

        for i in range(n - 1, -1, -1):  # Iterate through the heights array from right to left
            while stack and heights[i] > heights[stack[-1]]:  # While stack is not empty and current person is taller than the person at the top of the stack
                answer[i] += 1  # Increment the count of people the current person can see
                stack.pop()  # Remove the person at the top of the stack

            if stack:  # If stack is not empty
                answer[i] += 1  # Increment the count of people the current person can see (the person at the top of the stack)

            stack.append(i)  # Add the current person's index to the stack

        return answer  # Return the answer array
        