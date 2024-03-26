class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort() # Ascending order
        m = len(potions)
        
        for spell in spells:
            minPotion = (success + spell - 1) // spell
            
            # If min is greater than strongest, we dont care
            if minPotion > potions[-1]:
                ans.append(0)
                continue
                
            # Start binary search    
            bisectLeft = bisect.bisect_left(potions, minPotion) # We know where to at least start
            ans.append(m - bisectLeft)

        return ans