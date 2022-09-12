class Solution:
    def mergesort(self, nums1, nums2):
        if(len(nums1) == 0 and len(nums2) == 0):
            return nums1
        elif(len(nums1) == 0):
            return nums2
        elif(len(nums2) == 0):
            return nums1
        
        arr = []
        
        i = 0
        j = 0
        while(i != len(nums1) and j != len(nums2)):
            if(nums1[i] < nums2[j]):
                arr.append(nums1[i])
                i+=1
            elif(nums1[i] > nums2[j]):
                arr.append(nums2[j])
                j+=1
            else:
                arr.append(nums1[i])
                arr.append(nums2[j])
                i+=1
                j+=1
                
        while(i != len(nums1)):
            arr.append(nums1[i])
            i+=1
        while(j != len(nums2)):
            arr.append(nums2[j])
            j+=1
        return arr
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self.mergesort(nums1, nums2)
        if(len(arr) == 0):
            return None
        
        if(len(arr)%2 == 0):
             return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
        else:
            return arr[len(arr)//2]
