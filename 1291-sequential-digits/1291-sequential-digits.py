class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = "123456789"
        n = 10
        result = []
        
        # Iterate over all possible string lengths: from the length of low to the length of high.
        # Length is either 3
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                # 0, 1, 2, 3, 4, 5, 6
                num = int(base[start: start + length])
                if num >= low and num <= high:
                    result.append(num)
            
        return result