#Unsolved
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        arr = nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
        nums.clear()
        nums.extend(arr)
        #for i in range(0, len(arr)):
        #    nums.append(arr[i])
        #    nums.pop(0)
