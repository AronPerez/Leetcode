class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTER_MAP = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def backtrack(index, combination):
            if len(combination) == len(digits):
                result.append(''.join(combination))
                return

            for letter in LETTER_MAP[digits[index]]:
                combination.append(letter)
                backtrack(index + 1, combination)
                combination.pop()  

        if digits:
            backtrack(0, []) 
        return result
        