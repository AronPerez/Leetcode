class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): # If not the same length, we cannot swap just 2 chars
            return False
        
        if s == goal: # Identical strings or duplicates allow a trivial swap
            return not (len(set(s)) == len(s))
        
        if set(s) != set(goal): # Disallowed if they don't have the same set of characters
            return False
        
        """
        Difference Tracking: Creates a listmismatch_diffslst. The loop iterates through the strings comparing character by character. When differing characters are found
            Calculate Offset: It calculates the difference between the ASCII (ord) 
            values of the current mismatched characters (s[i], goal[i]) from the strings and appends it to lst.
            Checking Swappability: Immediately when len(lst) becomes 2 (means we found two character differences), two things are checked:
                Zero Sum: The elements in lst must sum to zero. This ensures the mismatches form a reverse pair for a correct swap, 
                (e.g., 'x' swapped with 'y', then 'y' must be swapped with 'x' in the correct positions
                Remaining Substring: The code tests if s[i+1:] == goal[i+1:], meaning the rest of the strings must exactly match after that position for a valid swap.
        """
        mismatch_diffs = []  # Store offset of mismatched characters for swap validation
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatch_diffs.append(ord(s[i]) - ord(goal[i]))
                if len(mismatch_diffs) == 2: 
                    return sum(mismatch_diffs) == 0 and s[i+1:] == goal[i+1:] 
        return False
        