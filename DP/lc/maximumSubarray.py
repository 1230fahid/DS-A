#Had to learn and implement kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnum = nums[0]
        sums = []
        sums.append(nums[0])
        for i in range(1, len(nums)):
            sums.append(0)
            sums[i] = max(nums[i], nums[i] + sums[i-1])
            if(sums[i] > maxnum):
                maxnum = sums[i]
        return maxnum
