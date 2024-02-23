class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = ans = sum(s[i] in vowels for i in range(k))
        
        # Can have a max of k vowels
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            ans = max(ans, count)
            
        return ans
            
        