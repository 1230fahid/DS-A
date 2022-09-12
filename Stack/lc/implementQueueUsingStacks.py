from collections import deque
class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        if(self.empty()):
            return
        i = len(self.stack1)-1
        self.stack2 = []
        while(i >= 0):
            self.stack2.append(self.stack1[i])
            i-=1
        #self.stack2 = self.stack1[::-1]
        num = self.stack2.pop()
        
        j = len(self.stack2)-1
        self.stack1 = []
        while(j >= 0):
            self.stack1.append(self.stack2[j])
            j-=1
            
        #self.stack1 = self.stack2[::-1]
        return num
    def peek(self) -> int:
        if(self.empty()):
            return
        return self.stack1[0]

    def empty(self) -> bool:
        if(len(self.stack1) == 0):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
