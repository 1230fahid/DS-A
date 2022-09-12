class Solution:
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
