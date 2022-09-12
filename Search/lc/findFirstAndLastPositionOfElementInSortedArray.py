class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) == 0):
            return [-1,-1]
        if(len(nums) == 1):
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        self.min = 100001
        self.max = -1
        self.binarySearch(nums, 0, len(nums)-1, target)
        if(self.min == 100001 and self.max == -1):
            return [-1,-1]
        else:
            return [self.min,self.max]
        
    def binarySearch(self, nums, begin, end, target):
        if(begin > end):
            return
        if(begin == end):
            mid = begin
        else:
            mid = (end - begin)//2 + 1 + begin
        if(nums[mid] < target):
            self.binarySearch(nums, mid+1, end, target)
        elif(nums[mid] > target):
            self.binarySearch(nums, begin, mid-1, target)
        else:
            if(mid < self.min):
                self.min = mid
            if(mid > self.max):
                self.max = mid
            self.binarySearch(nums, mid+1, end, target)
            self.binarySearch(nums, begin, mid-1, target)
