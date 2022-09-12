class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        j = len(nums)
        while(i < len(nums)-1):
            #print(i)
            if nums[i] == nums[i+1]:
                nums.pop(i)
                #print(nums)
                k+=1
                i-=1
                if(len(nums) == 1):
                    break
            i+=1
        print(k)
        return j-k
                
