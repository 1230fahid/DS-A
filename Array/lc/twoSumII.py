class Solution:
    #Input is sorted array, and there is always a sum of two numbers equal to target given
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lp = 0
        rp = len(numbers)-1
        while(lp != rp):
            if(numbers[lp] + numbers[rp] > target):
                rp -= 1
            elif(numbers[lp] + numbers[rp] < target):
                lp += 1
            else:
                return [lp+1, rp+1]
            
