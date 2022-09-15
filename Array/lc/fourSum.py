class Solution:
    #For this I tried using four pointers + hash set to check for previous array found. I want to do strictly with four pointer so I want to try and improve this. I know it's possible, since I was so close, but i'll come back to it later.

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if(len(nums) < 4):
            return []
        
        nums.sort()
        arr = []
        success1 = {}
        success2 = {}
        mydict = {}
        
        end = 0
        rp2 = 0
        
        
        for i in range(0, len(nums)):
            if(nums[i] in success1.keys()):
                continue
            #end += 1
            lp = i + 1
            rp1 = len(nums)-1
            rp2 = len(nums)-2
            mydict2 = {}
            iter = 0
            while (lp < rp2):
                while(lp < rp2):
                    if(nums[i] + nums[lp] + nums[rp2] + nums[rp1] < target):
                        lp += 1
                        while(nums[lp] == nums[lp-1]):
                            lp += 1
                            if(lp >= rp2 or lp == len(nums)):
                                break
                        
                    elif(nums[i] + nums[lp] + nums[rp2] + nums[rp1] > target):
                        rp2 -= 1
                        while(nums[rp2] == nums[rp2+1]):
                            rp2 -= 1
                            if(rp2 < 0 or rp2 <= lp):
                                break

                    else:
                        newarr = [nums[i], nums[lp], nums[rp2], nums[rp1]]
                        if(newarr not in mydict2.values()):
                            arr.append(newarr)
                            mydict2[iter] = newarr
                            iter+=1
                        
                        success1[nums[i]] = 0
                        lp += 1
                        while(nums[lp] == nums[lp-1]):
                            lp += 1
                            if(lp >= rp2 or lp == len(nums)):
                                break    
                        
                rp1 -= 1
                rp2 = rp1-1
                #while(nums[rp1] == nums[rp1+1]):
                #    rp1 -= 1
                #    rp2 = rp1-1
                #    if(lp > rp2):
                #        break
                #    if(nums[rp2] != nums[rp1]):
                #        break
                
                lp = i+1
            
        return arr                        
