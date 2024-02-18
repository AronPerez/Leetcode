class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
        1000, 900, 500, 400, 100,
        90, 50, 40, 10, 9, 5, 4, 1
        ]
        roman_numerals = [
            "M", "CM", "D", "CD", "C",
            "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]
        roman_number = ''
        i = 0
        while num > 0:
            for _ in range(num // values[i]):
                roman_number += roman_numerals[i]
                num -= values[i]
            i += 1
        return roman_number