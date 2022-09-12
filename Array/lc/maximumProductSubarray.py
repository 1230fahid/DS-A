class Solution:
    def getnegs(self, nums): #returns the first negative that appears in the list, and the last one that appears, as well as the total number of negative numbers in the array
        neg_nums = 0
        zeros = {}
        negatives = {}
        
        first_negative = None
        last_negative = None
        for i in range(0, len(nums)):
            if nums[i] < 0:
                if(len(negatives) == 0):
                    first_negative = i
                negatives[i] = 0
                last_negative = i
                neg_nums += 1 #count how many negative numbers appear
            elif nums[i] == 0:
                zeros[i] = 0 #get indexes of where zeros are
            #products.append(nums[i]) #get all individual numbers first just in case?
        return first_negative, last_negative, neg_nums
        
    def getmax(self, nums, first_negative, last_negative, neg_nums):
        if(len(nums) == 1):
            return nums[0]
        product = 1
        if(len(nums) == 0): #if array is empty then just return 0
            product = 0
        
        if(neg_nums == 0): #All positives, no negatives or zeros
            for i in nums:
                
                product *= i
        else: #no zeros, but negatives and positives
            if(neg_nums%2 == 0): #if even amount of negatives then you're fine
                for i in nums:
                    product *= i
            else:
                product1 = 1
                product2 = 1
                for i in range(0, last_negative):
                    product1 *= nums[i]
                for j in range(last_negative+1, len(nums)):
                    product2 *= nums[j]
                    
                product3 = 1
                product4 = 1
                for i in range(0, first_negative):
                    product3 *= nums[i]
                for j in range(first_negative+1, len(nums)):
                    product4 *= nums[j]
                product = max(product1, product2, product3, product4)
        return product
                    
    def maxProduct(self, nums: List[int]) -> int:        
        if(len(nums) == 1):
            return nums[0]
        products = []
        
        start = 0 #will want to get sub arrays up to each 0 found, or end of nums
        neg_nums = 0
        zeros = {}
        negatives = {}
        
        first_negative = None
        last_negative = None
        for i in range(0, len(nums)):
            if nums[i] < 0:
                if(len(negatives) == 0):
                    first_negative = i
                negatives[i] = 0
                last_negative = i
                neg_nums += 1 #count how many negative numbers appear
            elif nums[i] == 0:
                zeros[i] = 0 #get indexes of where zeros are
            products.append(nums[i]) #get all individual numbers first just in case?
        
        if(len(zeros) == 0):
            return self.getmax(nums, first_negative, last_negative, neg_nums) 
        else: #has zeros
            subarray = []
            zero_idxs = []
            for i in zeros.keys():
                zero_idxs.append(i)

            subarray = nums[0: zero_idxs[0]]
            start = 0
            if(len(subarray) != 0):
                first_negative, last_negative, neg_nums = self.getnegs(subarray)
                products.append(self.getmax(subarray, first_negative, last_negative, neg_nums))
            else:
                start = 1
            
            for i in range(0, len(zero_idxs)-1):
                subarray = nums[zero_idxs[i]+1:zero_idxs[i+1]]
                first_negative, last_negative, neg_nums = self.getnegs(subarray)
                products.append(self.getmax(subarray, first_negative, last_negative, neg_nums))
          
            subarray = nums[zero_idxs[len(zero_idxs)-1]+1:len(nums)]
            first_negative, last_negative, neg_nums = self.getnegs(subarray)
            products.append(self.getmax(subarray, first_negative, last_negative, neg_nums))
            
            return max(products)
            
        
        
        
