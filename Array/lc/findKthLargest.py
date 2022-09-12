class Solution:
    def merge_sort(self, nums):
        if len(nums)==1:
            return nums
        mid = len(nums)//2
        arr1 = self.merge_sort(nums[0:mid])
        arr2 = self.merge_sort(nums[mid:len(nums)])
        i=0
        j=0
        arr3=[]
        while(i<len(arr1) and j<len(arr2)):
            if(arr1[i] < arr2[j]):
                arr3.append(arr2[j])
                j+=1
            else:
                arr3.append(arr1[i])
                i+=1
        while(i < len(arr1)):
            arr3.append(arr1[i])
            i+=1
        while(j < len(arr2)):
            arr3.append(arr2[j])
            j+=1
        return arr3
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=self.merge_sort(nums)
        print(arr)
        return arr[k-1]
