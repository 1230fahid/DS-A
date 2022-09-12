# Had to get help from youtube. Please go over this and try to understand in depth. Creating a DAG to visualize helps. Remember the 5 steps
# This is the youtube help: https://www.youtube.com/watch?v=aPQY__2H3tE

class Solution:
    def length(self, arr, nums, index):
        maxs = []
        for i in range(0, index):
            if(nums[i] < nums[index]):
                maxs.append(arr[i])
        if(len(maxs) != 0):
            arr[index] += max(maxs)
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        maxs = 0
        mydict = {}
        iters = 1
        #index = 0
        for i in range(1, len(nums)):
            self.length(arr, nums, i)
        
        #print(arr)
        return max(arr)

#This solution is an iterative approach. We knew what our base case was, and since we were moving forward by each index, looking for the longest increasing subsequence for each index, we relied on previous values, which were calculate and stored in an array before the current index. Using that, we then appended all values that connected to the current value, found the max of that, and added it to the current index of the array
