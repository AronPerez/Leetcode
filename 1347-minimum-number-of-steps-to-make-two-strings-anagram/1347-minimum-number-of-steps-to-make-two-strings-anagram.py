class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCharFreq = Counter(s)
        tCharFreq = Counter(t)
        
        # If all the values from s are in s, we have Anagram
        if sCharFreq == tCharFreq:
            return 0
        
        steps = 0
        
        for key, value in tCharFreq.items():
            if sCharFreq[key] < value: # If the corresponding value in s is less than t, we can increment changes
                steps += value - sCharFreq[key] # The diff of values in t - s is how many changes we need to make to match
        
        
        return steps