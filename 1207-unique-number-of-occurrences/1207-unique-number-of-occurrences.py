class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numFreq = Counter(arr)
        seenFreq = set()
        
        for num, freq in numFreq.items():
            if freq not in seenFreq: # Not seen, we can continue
                seenFreq.add(freq)
            else: # Freq has been seen, we return false
                return False
            
        return True
                
        