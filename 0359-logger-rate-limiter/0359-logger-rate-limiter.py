class Logger:

    def __init__(self):
        # Use a hashtable/dict where the message is the key
        # Timestmap would be the value
        self.messages = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool: # Not seen, add to dict and key is timestamp
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        
        # If we are here, we can assume the message key is in the dict
        if timestamp - self.messages[message] >= 10: # If 10 or more secs has elapsed since the last time the key was logged
            self.messages[message] = timestamp
            return True
        else:
            return False
       
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)