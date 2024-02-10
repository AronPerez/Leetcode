class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): # If not the same length, we cannot swap just 2 chars
            return False
        
        if s == goal: # Identical strings or duplicates allow a trivial swap
            return not (len(set(s)) == len(s))
        
        if set(s) != set(goal): # Disallowed if they don't have the same set of characters
            return False
        
        mismatch_diffs = []  # Store offset of mismatched characters for swap validation
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatch_diffs.append(ord(s[i]) - ord(goal[i]))
                if len(mismatch_diffs) == 2: 
                    return sum(mismatch_diffs) == 0 and s[i+1:] == goal[i+1:] 
        return False
        