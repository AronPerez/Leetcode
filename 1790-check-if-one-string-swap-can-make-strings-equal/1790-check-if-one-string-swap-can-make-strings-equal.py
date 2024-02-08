class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1CharFreq = Counter(s1)
        s2CharFreq = Counter(s2)
        
        if s1CharFreq != s2CharFreq: # Is impossible to swap since not all chars needed in s1 are in s2 or vice versa
            return False
        
        # We can at most swap 1, which means at most 2 strings cannot be the same
        diff = i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                diff += 1
                
            i += 1
        
        if diff == 2 or diff == 0:
            return True
        else:
            return False
        