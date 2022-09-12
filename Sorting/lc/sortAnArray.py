class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) == 1):
            return nums
        l1=self.sortArray(nums[0:len(nums)//2])
        r1=self.sortArray(nums[len(nums)//2:len(nums)])
        i=j=0
        nums = []
        while((i < len(l1)) and (j < len(r1))):
            if l1[i] < r1[j]:
                nums.append(l1[i])
                i+=1
            else:
                nums.append(r1[j])
                j+=1
        while(i < len(l1)):
            nums.append(l1[i])
            i+=1
        while(j < len(r1)):
            nums.append(r1[j])
            j+=1
        return nums
