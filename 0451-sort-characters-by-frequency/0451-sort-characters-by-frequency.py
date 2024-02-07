class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = Counter(s).most_common()
        s = ""    
        
        for value, freq in charFreq:
            s += value * freq
        
        return s