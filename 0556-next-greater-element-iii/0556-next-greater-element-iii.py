class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Explanation:
        1. Convert n to a list of digits
        2. Find the first digit from the right that is smaller than its next digit
        3. If no such digit is found, return -1
        4. Find the smallest digit to the right of the found digit that is greater than it
        5. Swap the two digits
        6. Reverse the remaining digits to the right of the swapped digit
        7. Convert the list back to an integer
        8. Check for 32-bit overflow and return the integer or -1
        """
        digits = list(str(n))  # Convert n to a list of digits

        i = len(digits) - 2  # Start from the second-last digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1  # Find the first digit that is smaller than its next digit
            
        if i == -1:
            return -1  # No such larger integer exists

        j = i + 1  # Find the smallest digit greater than digits[i] to the right of i
        while j < len(digits) and digits[j] > digits[i]:
            j += 1
        # 230241/2,1
        print(i, j)
        # digits[3], digits[4] = 230421
        digits[i], digits[j - 1] = digits[j - 1], digits[i]  # Swap digits[i] and digits[j-1]
        # 4:5 = 21 = 12
        digits[i + 1:] = digits[i + 1:][::-1]  # Reverse the digits after i (in-place)

        nextGreater = int("".join(digits))  # Convert the list back to an integer
        return nextGreater if nextGreater <= 2**31 - 1 else -1  # Check for 32-bit overflow
        