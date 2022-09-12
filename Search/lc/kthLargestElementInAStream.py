class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        if(len(nums) > 0):
            self.nums.append(nums[0])
            for i in range(1, len(nums)):
                if(self.nums[0] >= nums[i]):
                    self.nums.insert(0, nums[i])
                elif(self.nums[len(self.nums)-1] <= nums[i]):
                    self.nums.append(nums[i])
                else:
                    self.binarySearch(self.nums, nums[i], 0, len(self.nums)-1)
        
    def binarySearch(self, nums, val, begin, end):
        if(begin >= end):
            return
                    
        mid = (end-begin)//2 + begin

        if(val < nums[mid]):
            if(val >= nums[mid-1]):
                nums.insert(mid, val)
            else:
                self.binarySearch(nums, val, begin, mid-1)
        elif(val > nums[mid]):
            if(val <= nums[mid+1]):
                nums.insert(mid+1, val)
            else:
                self.binarySearch(nums, val, mid+1, end)
        else:
            nums.insert(mid, val)
        
    def add(self, val: int) -> int:
        if(len(self.nums) == 0):
            self.nums.append(val)
        elif(self.nums[0] >= val):
            self.nums.insert(0, val)
        elif(self.nums[len(self.nums)-1] <= val):
            self.nums.append(val)
        else:
            self.binarySearch(self.nums, val, 0, len(self.nums)-1)
        
        return self.nums[len(self.nums)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
