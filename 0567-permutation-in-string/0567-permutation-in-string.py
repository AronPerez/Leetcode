class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:     
        n1 = len(s1)
        n2 = len(s2)
        
        # s2 is too small for a permutation of s1 to exist
        if n1 > n2: return False
        
        # Array maps
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Init values for first set of window
        for i in range(n1):
            # Goes through first n1 chars of s2
            # Get ASCII value of char - lowercase of a, will map to 0-25
            # a = 0, b = 1, c = 2..
            s1Count[ord(s1[i]) - ord('a')] += 1 # Update freq in array to 1
            s2Count[ord(s2[i]) - ord('a')] += 1 # Update freq in array to 1
           
        # Initialize matches
        matches = 0
        for i in range(26): # 26 spots in arr since 26 chars
            matches += (1 if s1Count[i] == s2Count[i] else 0)
            
        # Sliding window
        l = 0
        # Since we already init our array with len n1, we just need to go
        # n1 - n2
        for r in range(n1, n2):
            if matches == 26: return True # We found permutation of s1 at front of s2
            
            # Right side of window
            index = ord(s2[r]) - ord('a') # Index in array of char (0-25)
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]: # If made exactly equal, we have a match
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # Means they WERE equal, but now are unequal
                matches -= 1
            
            # Left side of window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 # Char just removed from left side of window

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # Removing the char from window made it unequal
                matches -= 1
            
            l += 1 
        
        return matches == 26
                        
                        