class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True # Already palindrome

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Check if removing left or right char makes it palindrome
                if s[l + 1:r + 1] ==  s[l + 1:r + 1][::-1]: # Remove left char
                    return True
                elif s[l:r] ==  s[l:r][::-1]: # Remove right char
                    return True
                else: # No palindrome possible
                    return False
            l += 1
            r -= 1
        return False # Cannot reach here
        