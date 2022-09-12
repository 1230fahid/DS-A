class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.cQueue = []

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        else:
            self.cQueue.append(value)
            return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        else:
            self.cQueue.pop(0)
            return True

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        else:
            return self.cQueue[0]
            

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        else:
            return self.cQueue[len(self.cQueue)-1]
            

    def isEmpty(self) -> bool:
        if(len(self.cQueue) == 0):
            return True
        else:
            return False

    def isFull(self) -> bool:
        if(len(self.cQueue) == self.size):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
