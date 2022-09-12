class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer=-1
        twoPointer = len(nums)
        i=0
        newarr = []
        while i < len(nums):
            #print("nums before ", nums)
            if nums[i] == 0:
                #nums.pop(i)
                newarr.append(0)
            
            i+=1
        
        i = 0
        while i < len(nums):
            #print("nums before ", nums)
            if nums[i] == 1:
                #nums.pop(i)
                newarr.append(1)
            i+=1
        
        i = 0
        while i < len(nums):
            #print("nums before ", nums)
            if nums[i] == 2:
                #nums.pop(i)
                newarr.append(2)
            i+=1
        
        i = 0
        while i < len(newarr):
            nums.append(newarr[i])
            nums.pop(0)
            i+=1
            
                
