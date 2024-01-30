class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans * 26 # Base 26
            # A's ASCII is 0, take letter - 0 to get value
            # B - A = 2
            ans += (ord(columnTitle[i]) - ord('A') + 1)
        return ans