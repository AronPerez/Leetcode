class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        # Base case: all single-character substrings are palindromes
        for i in range(n):
            dp[i][i] = True

        # Fill in the table in bottom-up manner
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        # Find the longest palindrome substring
        start = 0
        max_len = 1
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]