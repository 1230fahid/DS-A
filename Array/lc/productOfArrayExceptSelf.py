class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros[i] = 0        
        if(len(zeros) > 1):
            return [0]*len(nums)
        elif(len(zeros) == 0):
            answer = []
            product = 1
            for i in range(0, len(nums)):
                product *= nums[i]
            for i in range(0, len(nums)):
                answer.append(product//nums[i])
            return answer
        else:
            answer = []
            product = 1
            key = 0
            for i in range(0, len(nums)):
                if(i in zeros.keys()):
                    key = i
                    continue
                else:
                    product *= nums[i]
            
            #zeros[key] = product
            
            for i in range(0, len(nums)):
                if i == key:
                    answer.append(product)
                else:
                    answer.append(0)
            return answer
