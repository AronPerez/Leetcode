class MyQueue:

    def __init__(self):
        self.stack = []
        self.removalStack = []


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.removalStack: 
            while self.stack:
                self.removalStack.append(self.stack.pop())
        
        return self.removalStack.pop()

    def peek(self) -> int:
        if not self.removalStack:
            while self.stack:
                self.removalStack.append(self.stack.pop())
        
        return self.removalStack[-1]

    def empty(self) -> bool:
        return not self.stack and not self.removalStack # If 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()