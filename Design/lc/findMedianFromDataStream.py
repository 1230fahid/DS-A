class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if(len(self.arr) == 0):
            self.arr.append(num)
        elif(num >= self.arr[len(self.arr)-1]):
            self.arr.append(num)
        elif(num <= self.arr[0]):
            self.arr.insert(0,num)
        else:
            self.binarySearch(num, 0, len(self.arr)-1)
    def findMedian(self) -> float:
        if(len(self.arr) == 2):
            return (self.arr[0] + self.arr[1])/2.0
        elif(len(self.arr)%2 != 0):
            return self.arr[len(self.arr)//2]
        else:
            return (self.arr[len(self.arr)//2] + self.arr[len(self.arr)//2 - 1])/2.0
        
    def binarySearch(self, num, begin, end):
        if(begin >= end):
            if(self.arr[begin] >= num):
                self.arr.insert(begin, num)
            else:
                self.arr.insert(begin+1, num)
        elif(self.arr[(end-begin)//2 + begin] == num):
            self.arr.insert((end-begin)//2 + begin+1, num)
            return
        elif(self.arr[(end-begin)//2 + begin] > num):
            self.binarySearch(num, begin, (end-begin)//2 + begin-1)
        elif(self.arr[(end-begin)//2 + begin] < num):
            self.binarySearch(num, (end-begin)//2 + begin+1, end)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
