class FileSystem:

    def __init__(self):
        self.directory = {}
        
    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or len(path) == 0 or path in self.directory:
            return False
        else: 
            parent = path[:path.rfind('/')]
            
            if len(parent) > 1 and parent not in self.directory:
                return False
            
            self.directory[path] = value
            return True

    def get(self, path: str) -> int:
        return self.directory.get(path, -1)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)