class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] not in mydict.keys():
                mydict[nums[i]] = 1
            else:
                mydict[nums[i]] += 1
        
        
        arr = []
        maxs = 0
        for i in range(0,k):
            maxs = 0
            savekey = None
            for key in mydict.keys():
                if mydict[key] > maxs:
                    maxs = mydict[key]
                    savekey = key
            
            arr.append(savekey)
            del mydict[savekey]
        
        return arr
