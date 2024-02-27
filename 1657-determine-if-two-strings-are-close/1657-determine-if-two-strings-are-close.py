class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1CharFreq = Counter(word1) # {'a': 1}
        word2CharFreq = Counter(word2)
        
        freq1 = Counter([value for value in word1CharFreq.values()]) # {1: 1} The 1 freq appears 1 time
        freq2 = Counter([value for value in word2CharFreq.values()])
        
        return word1CharFreq == word2CharFreq or (freq1 == freq2 and set(word1) == set(word2))
        
        
        
        
        