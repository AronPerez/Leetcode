class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Always in pairs of 2
        
        """
            pairs = Counter()
            {
            'aa': 2,
            'ab':2,
            'ba':3,

            }
            ab ba ab ba
            
            for key, value in pairs.items()
            
            if key[0] == key[1]: # aa
                totalLen += 1
                continue
            
            Take the min of the two, add it to len
            minOfPair * 2 = 4
            
            Once we have checked these, we can add to a seen set
            {'ab'}
            
            
            dd 5
            aa 3
            bb 3
            cc 3
            
            10
            
            2, 4, 6, 8, 10, 12, 14, 16 aa
            4, 8, 12, 16, 20 ab ba
            
            aa: 1
            bb: 1
            
            
            1, 3, 5, 7
            2, 6, 10, 14
            
            dd dd dd dd dd 10 / 2 = 5
            dd dd aa dd aa dd dd 14 / 2 = 7
            dd bb dd aa dd aa dd bb dd 18 / 2 = 9
            
            if value % 2 == 1
            Counter({'em': 3, 'me': 2, 'pe': 1, 'mp': 1, 'ee': 1, 'pp': 1, 'ep': 1})
        """
        
        
        wordFreq = Counter(words)
        seen = set()
        totalLen = 0
        centralized = False
        
        for key, value in wordFreq.items():
            if key in seen: # Have seen if before, keep going
                continue
            
            if key == key[::-1]: # aa
                if value % 2 == 0: # Is even freq
                    totalLen += value
                else: # Is odd freq
                    totalLen += (value-1) # cannot have odd value
                    centralized = True
                
                continue
                
            # Check if key has compliment
            possibleComplient = wordFreq.get(key[::-1])
            if possibleComplient:
                totalLen += min(value, possibleComplient) * 2 # len if pair is 4
                seen.add(key[::-1])
            
        if centralized:
            totalLen += 1
        
        return totalLen * 2
                
                
            
                