class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # every char in t must be in window of s
        n = len(s)
        m = len(t)
        # What if the len of t is greater than s, then we return ""
       
        
        if m > n or t == "":
            return ""
        
        # Need a freq of chars for t
        # Freq of chars 
        tCharFreq = Counter(t)
        windowCharFreq = defaultdict(int)
        
        have, need = 0, len(tCharFreq)
        res, resLen = [-1, -1], float('inf')
        # look at a window that is at min the len of t
        # l , r = 0, m-1
        l = 0
        # Some way to keep track of the values with the min window substring
        # The first result we find, we only want to find ans smaller than it
        
        # while r < n:
            # Check the values in window l to r
            # We want their freq
            # for i in range(l, r):
               #  windowCharFreq[s[i]] += 1
            
            # We need to remove values as we resize
            
            # If we have at least 1 value, we keep expanding the right pointer,
            # Keep track of the min substring how?
        
        for r in range(n):
            # The char
            c = s[r]
            
            # Check the values in window l to r
            # We want their freq
            windowCharFreq[c] += 1
            
            if c in tCharFreq and windowCharFreq[c] == tCharFreq[c]: # Only care if char is in tCharFreq
                have += 1 # We have at least 1 value
                
            while have == need:
                tempResLen = (r - l + 1)
                if tempResLen < resLen: # Update result with new min
                    res = [l, r]
                    resLen = tempResLen
                # Pop from l of the window
                windowCharFreq[s[l]] -= 1
                # If by removing char, we took our have, and decremented it by 1
                if s[l] in tCharFreq and windowCharFreq[s[l]] < tCharFreq[s[l]]:
                    have -= 1
                l += 1
                    
        
        # return the min substring
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
            
                