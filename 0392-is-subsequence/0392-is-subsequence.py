class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        j = 0
        m = len(s)
        
        for i in range(len(t)):
            if j < m and t[i] == s[j]:
                j += 1
                
        return True if j == m else False
        