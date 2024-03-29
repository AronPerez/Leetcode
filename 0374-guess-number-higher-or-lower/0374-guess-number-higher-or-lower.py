# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            m = l + (r - l) // 2
            
            pick = guess(m)
            
            if pick == 0:
                return m
            elif pick < 0: # to the left
                r = m - 1
            else: # to the right
                l = m + 1
                
                
        return -1
        