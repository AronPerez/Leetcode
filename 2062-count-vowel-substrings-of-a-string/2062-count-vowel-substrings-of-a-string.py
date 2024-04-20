class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans, n = 0, len(word)
        # aeiouu
        # Start word string search
        for l in range(n): 
            # If we see a vowel, then we start substring window search
            if word[l] in vowels: # a
                r, seen = l+1, {word[l]} # 1, {}
                """
                true, 'e' true
                {'a', 'e'}
                false
                2
                
                true, 'i' true
                {'a', 'e', 'i'}
                false
                3
                
                true, 'o' true
                {'a', 'e', 'i', 'o'}
                false
                4
                
                true, 'u' true
                {'a', 'e', 'i', 'o', 'u'}
                true
                1
                5
                
                true, 'u' true
                {'a', 'e', 'i', 'o', 'u'}
                true
                2
                6
                
                2
                """
                while r < n and word[r] in vowels: 
                    seen.add(word[r]) # Add to set 
                    # Check if all vowels are in substring
                    if seen ^ vowels == set(): # If all vowels are in seen
                        ans += 1 # Increment ans
                    r += 1

        return ans
            
                
        