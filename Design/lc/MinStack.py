class MinStack:

    def __init__(self):
        self.st = []
        self.mins  = [] 

    def push(self, val: int) -> None:
        if(len(self.mins) == 0):
            self.mins.append(val)
        elif(val <= self.mins[len(self.mins)-1]):
            self.mins.append(val)
        self.st.append(val)

    def pop(self) -> None:
        if(len(self.st) == 0):
            return
        if(self.st[len(self.st)-1] == self.mins[len(self.mins)-1]):
            self.mins.pop()
        num = self.st[len(self.st) - 1]
        self.st.pop()

    def top(self) -> int:
        return(self.st[len(self.st) - 1])

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
