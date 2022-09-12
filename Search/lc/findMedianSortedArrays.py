class Solution:
    def __init__(self):
        self.count = 0
        self.val = 0
    def median(self, l):
        if(len(l) == 2):
            print("This was done")
            median = (l[0] + l[1]) / 2.0
            print("Median is: {}".format(median))
            return float (median)
        else:
            print("No this was done")
            return float(l[0])
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1) > 1000 or len(nums2) > 1000):
            return
        if(len(nums1) > 0 and len(nums2) > 0):
            if(max(nums1) > 1000000 or max(nums2) > 1000000):
                return
            if(min(nums1) < -1000000 or min(nums2) < -1000000):
                return
        elif(len(nums1) > 0 and len(nums2) <= 0):
            if(max(nums1) > 1000000):
                return
            if(min(nums1) < -1000000):
                return
        elif(len(nums1) <= 0 and len(nums2) > 0):
            if(max(nums2) > 1000000):
                return
            if(min(nums2) < -1000000):
                return
        l = nums1 + nums2
        l.sort()
        #print(l)
        print(len(l))
        num = 0
        if(len(l) <= 2):
            self.count = len(l)
            self.val=median(l)
            pass
        else:
            l.pop(0)
            l.pop()
            new_len=int(len(l)/2)
            tail = l[new_len:]
            head = l[:new_len]
            self.findMedianSortedArrays(tail, head)
        return(self.val)
