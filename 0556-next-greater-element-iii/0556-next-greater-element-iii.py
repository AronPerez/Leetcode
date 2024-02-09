class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))  # Convert n to a list of digits

        i = len(digits) - 2  # Start from the second-last digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1  # Find the first digit that is smaller than its next digit

        if i == -1:
            return -1  # No such larger integer exists

        j = i + 1  # Find the smallest digit greater than digits[i] to the right of i
        while j < len(digits) and digits[j] > digits[i]:
            j += 1

        digits[i], digits[j - 1] = digits[j - 1], digits[i]  # Swap digits[i] and digits[j-1]
        digits[i + 1:] = digits[i + 1:][::-1]  # Reverse the digits after i (in-place)

        next_greater = int("".join(digits))  # Convert the list back to an integer
        return next_greater if next_greater <= 2**31 - 1 else -1  # Check for 32-bit overflow
        