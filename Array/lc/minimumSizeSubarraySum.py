class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mins = (10**5) + 1
        arr = []
        sum = 0
        sumcheck = 0
        
        for i in range(0, len(nums)):
            sum += nums[i]
            sumcheck += nums[i]
            arr.append(nums[i])
            while (sum >= target):
                if(len(arr) < mins):
                    mins = len(arr)
                sum -= arr.pop(0)
        
        
        if(sumcheck < target):
            return 0
        else:
            return mins
