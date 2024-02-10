class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If not the same length, we cannot swap just 2 chars
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return not (len(set(s)) == len(s))
        
        if set(s) != set(goal):
            return False
        
        
        lst = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                lst.append(ord(s[i]) - ord(goal[i]))
                if len(lst) == 2:
                    return s[i+1:] == goal[i+1:] if sum(lst) == 0 else False 
        return False
        