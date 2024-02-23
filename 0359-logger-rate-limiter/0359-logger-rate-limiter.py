class Logger:

    def __init__(self):
        self.messageSet = set()
        self.messageQueue = deque()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.messageQueue:
            msg, ts = self.messageQueue[0]
            if timestamp - ts >= 10: # If 10 seconds have elapsed
                self.messageQueue.popleft()
                self.messageSet.remove(msg)
            else: # 
                break
                
        if message not in self.messageSet: # If msg not seen before, we can log it
            self.messageSet.add(message)
            self.messageQueue.append((message, timestamp))
            return True
        else:
            return False
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)