class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        arr = []
        if(nums[0] < nums[len(nums)-1]):
            return nums[0]
        self.rotateBinarySearch(nums, 0, len(nums)-1, arr)
        return arr[0]
        
    def rotateBinarySearch(self, nums, start, end, arr):
        if(start >= end):
            return -1
        mid = (end - start)//2 + start
        if(mid == 0):
            mid+=1
        if(nums[mid-1] > nums[mid]):
            arr.append(nums[mid])
            return
        elif(nums[mid+1] < nums[mid]):
            arr.append(nums[mid+1])
        
        if(len(arr) > 0):
            return
        left = self.rotateBinarySearch(nums,start, mid-1, arr)
        if(len(arr) > 0):
            return
        right = self.rotateBinarySearch(nums,mid+1, end, arr)

