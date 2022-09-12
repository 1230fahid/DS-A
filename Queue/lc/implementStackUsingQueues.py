class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)  #[1,2,3,4,5]
        self.queue2.insert(0, x) #[5,4,3,2,1]

    def pop(self) -> int:
        num = self.queue2.pop(0) #[4,3,2,1]
        self.queue1 = self.queue2[::-1] #[1,2,3,4]
        return num

    def top(self) -> int:
        return self.queue1[len(self.queue1)-1]

    def empty(self) -> bool:
        if(len(self.queue1) == 0) or (len(self.queue2) == 0):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
