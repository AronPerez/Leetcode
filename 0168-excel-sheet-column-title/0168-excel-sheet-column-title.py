class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber -= 1 # Accounts for 0 based indexing
            # Get mod 26 of value + ASCII value A which is 0
            title = chr(columnNumber % 26 + ord('A')) + title
            columnNumber //= 26
        return title