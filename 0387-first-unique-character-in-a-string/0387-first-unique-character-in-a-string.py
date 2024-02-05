class Solution:
    def firstUniqChar(self, s: str) -> int:
        charFreq = Counter(s)
        
        for index, char in enumerate(s):
            if charFreq[char] == 1:
                return index
        
        return -1