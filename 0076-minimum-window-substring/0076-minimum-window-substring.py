class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = collections.Counter(t)  # Character counts needed from t
        missing = len(t)  # Characters still needed to complete t
        left = right = 0  # Pointers for sliding window
        min_window = float('inf'), None, None  # Initialize minimum window

        while right < len(s):
            c = s[right] 
            if c in need:
                need[c] -= 1
                if need[c] >= 0:  # Only count characters that are still needed
                    missing -= 1

            while missing == 0:  # Shrink window if possible
                c = s[left]
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                if c in need:
                    need[c] += 1
                    if need[c] > 0:  # Stop shrinking if a character is no longer sufficient
                        missing += 1
                
                if right - left + 1 < min_window[0]: # Save the smallest window until now.
                    min_window = (right - left + 1, left, right)
                
                # Move the left pointer ahead, this would help to look for a new window.                    
                left += 1
            
            # Keep expanding the window once we are done contracting.
            right += 1

        return "" if min_window[0] == float('inf') else s[min_window[1]:min_window[2] + 1]
                           
        