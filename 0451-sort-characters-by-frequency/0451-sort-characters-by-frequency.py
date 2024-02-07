class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = Counter(s)
        
        sortedCharFreq = sorted(charFreq, key=charFreq.get, reverse=True)
        
        s = ""    
        
        for char in sortedCharFreq:
            s += char * charFreq[char]
        
        return s