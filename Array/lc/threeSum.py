class Solution2: #better runtime, passes each time. Still want to improve.
    #for this i did did the two sum 2 problem for each index
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right = {}
        left = {}
        success = {}
        arr = []
        nums.sort()
        
        for i in range(0, len(nums)):
            if(nums[i] in success.keys()):
                continue
            lp = i+1
            rp = len(nums)-1
            while(lp < rp):
                if(nums[i] + nums[lp] + nums[rp] < 0):
                    lp += 1
                    while(nums[lp] == nums[lp-1]):
                        lp+=1
                        if(lp == len(nums)):
                            break
                elif(nums[i] + nums[lp] + nums[rp] > 0):
                    rp -= 1
                    while(nums[rp] == nums[rp+1]):
                        rp-=1
                        if(rp < 0):
                            break
                else:
                    arr.append([nums[i], nums[lp], nums[rp]])
                    success[nums[i]] = 1
                    lp+=1
                    while(nums[lp] == nums[lp-1]):
                        lp+=1
                        if(lp == len(nums)):
                            break
                    
        return arr


class Solution:#slow. Can sometimes fail and sometimes pass
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return None
        answers = {}
        three_sum = []
        k = 0
        for i in range(0, len(nums)):
            lookup = {} #clears lookup and restarts process
            for key, val in enumerate(nums[i+1:]):
                if val in lookup.keys(): #checks if the final value needed to sum 0 in the lookup
         #           print(lookup[val])
                    arr = [nums[i], val, lookup[val]]
                    arr = sorted(arr)
                    if arr in answers.values():
                        continue
                    else:
                        answers[k] = arr
                        three_sum.append(arr)
                        k+=1
          #          print(lookup)
                else:
                    #store the remainder here
                    lookup[-val-nums[i]] = val
        #print(answers)

        return three_sum
