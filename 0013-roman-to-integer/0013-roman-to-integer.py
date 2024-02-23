class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their corresponding integer values.
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Initialize the running total to 0.
        total = 0

        # Iterate through the string of Roman numerals from left to right.
        for i in range(len(s)):
            # Look up the value of the current Roman numeral in the dictionary.
            value = roman_numerals[s[i]]

            # If the current Roman numeral is less than the next Roman numeral, then it is a subtraction.
            if i + 1 < len(s) and value < roman_numerals[s[i + 1]]:
                # Subtract the value of the current Roman numeral from the running total.
                total -= value
            # Otherwise, it is an addition.
            else:
                # Add the value of the current Roman numeral to the running total.
                total += value

        # Return the running total.
        return total
