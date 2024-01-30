class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Converts to lowercase
        s = s.lower()
        # Strips whitespace
        s = s.replace(" ", "")
        s = re.sub(r'[^a-z0-9]', "", s)
        print(s)

        if s == s[::-1]:
            return True
        return False
        