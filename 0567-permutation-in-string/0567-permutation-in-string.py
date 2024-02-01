class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        # Need to generate permutations of s1
        # counter = {'a': 1, 'b': 1}
        # window = 2
        # matches = 0
        counter, window, matches = Counter(s1), len(s1), 0

        #  s1 = "ab", s2 = "eidbaooo"
        for i in range(len(s2)):
            if s2[i] in counter: 
                counter[s2[i]] -= 1 # Since we are moving out of the window, remove match
                if counter[s2[i]] == 0:
                    matches += 1
            # 0 > 2 and s[-2] in counter, 1 > 2 and s[-1] in counter
            # 2 > 2 and s[0] in counter, 3 > 2 and s[1] in counter
            print(i-window)
            if i >= window and s2[i-window] in counter:
                if counter[s2[i-window]] == 0:
                    matches -= 1
                counter[s2[i-window]] += 1
            
            if matches == len(counter):
                return True
        
        return False
                        
                        