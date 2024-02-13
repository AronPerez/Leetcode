class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        if timestamp < self.store[key][0][0]: # If the timestamp is less than first timestamped, no ans
            return ""
        r = self.binarSearchHelper(key, timestamp)
        return "" if r == 0 else self.store[key][r - 1][1]
    
    def binarSearchHelper(self, key: str, timestamp: int) -> int:
        l, r = 0, len(self.store[key])
        
        while l < r:
            m = l + (r - l) // 2
            
            if self.store[key][m][0] <= timestamp: # Value is likely on right
                l = m + 1
            else: # Value is likely on left
                r = m
 
        return r
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)