class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(nums[0] == target):
            return 0
        if(nums[len(nums)-1] == target):
            return len(nums)-1
        arr = []
        if(nums[0] < nums[len(nums)-1]):
            self.binarySearch(nums, 0, len(nums)-1, target, arr)
            arr.append(-1)
            return arr[0]
        else:
            self.rotatedBinarySearch(nums, 0, len(nums)-1, target, arr)
            arr.append(-1)
            return arr[0]
        
    def binarySearch(self, nums, begin, end, target, arr):
        if(len(arr) > 0):
            return
        if(begin == end):
            if nums[begin] == target:
                arr.append(begin)
            return
        if(begin > end):
            return
        mid = ((end-begin)//2) + begin
        if(nums[mid] == target):
            arr.append(mid)
            return
        elif(target < nums[mid]):
            self.binarySearch(nums, begin, mid-1, target, arr)
        elif(target > nums[mid]):
            self.binarySearch(nums, mid+1, end, target, arr)
            
            
    def rotatedBinarySearch(self, nums, begin, end, target, arr):
        if(len(arr) > 0):
            return
        if(begin >= end):
            return
        mid = ((end-begin)//2) + begin
        
        if(nums[mid] == target):
            arr.append(mid)
            return
        
        if(nums[mid-1] > nums[mid]) or (nums[mid+1] < nums[mid]):
            range1_b = nums[begin]
            range1_e = nums[mid-1]
            range2_b = nums[mid+1]
            range2_e = nums[end]
            if(range1_b <= target) and (target <= range1_e):
                self.binarySearch(nums, begin, mid-1, target, arr)
            elif((range2_b <= target) and (target <= range2_e)):
                self.binarySearch(nums, mid+1, end, target, arr)
        
        elif(nums[0] < nums[mid-1]) and (nums[mid+1] > nums[end]):
            range1_b = nums[begin]
            range1_e = nums[mid-1]
            if(range1_b <= target) and (target <= range1_e):
                self.binarySearch(nums, begin, mid-1, target, arr)
            else:
                self.rotatedBinarySearch(nums, mid+1, end, target, arr)
        elif(nums[0] > nums[mid-1]) and (nums[mid+1] < nums[end]):
            range2_b = nums[mid+1]
            range2_e = nums[end]
            if(range2_b <= target) and (target <= range2_e):
                self.binarySearch(nums, mid+1, end, target, arr)
            else:
                self.rotatedBinarySearch(nums, begin, mid-1, target, arr)
