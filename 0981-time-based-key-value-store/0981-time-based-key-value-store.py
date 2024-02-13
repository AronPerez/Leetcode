from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = SortedDict()

        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        iterator = self.store[key].bisect_right(timestamp)
        if iterator == 0:
            return ""
        
        return self.store[key].peekitem(iterator - 1)[1]
 
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)