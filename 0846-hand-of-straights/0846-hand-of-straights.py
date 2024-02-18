class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Input is not sorted to begin with
        cardFreq = Counter(hand)
        keys = sorted(cardFreq) # Ascending order, 
        
        # We need to get the groups
        # Cannot have dupes in group, no 1, 1, 2 
        
        for key in keys:
            if cardFreq[key] > 0:
                for i in range(groupSize-1, -1, -1):
                    if key + i not in cardFreq:
                        return False
                    
                    cardFreq[key + i] -= cardFreq[key]
                    
                    
                    if cardFreq[key + i] < 0:
                        return False
                    
        return True
        
            
            