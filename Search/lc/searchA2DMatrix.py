class Solution3:
    #Same as solution 2, but iterative, so space complexity should be constant. If I am wrong, I'd love to know what is wrong with my reasoning.

    def binarySearchMatrix(self, target, matrix, begin, end):
        while(begin <= end):
            if(begin > end):
                return -1
            if (begin == end):
                if matrix[begin][0] <= target and target <= matrix[begin][len(matrix[begin])-1]:
                    return begin
                else:
                    return -1
            
            mid = (end-begin)//2 + begin
        
            if(matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid])-1]):
                return mid
        
            elif(target < matrix[mid][0]):
                end = mid-1
            elif(target > matrix[mid][len(matrix[mid])-1]):
                begin = mid+1                
        
        return -1
        
    def binarySearch(self, target, array, begin, end):
        while(begin <= end):        
            if begin == end:
                if array[begin] == target:
                    return True
                else:
                    return False
            
            mid = (end-begin)//2 + begin
        
            if(array[mid] == target):
                return True
        
            elif(target < array[mid]):
                end = mid-1
            elif(target > array[mid]):
                begin = mid+1
                
        return False
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.binarySearchMatrix(target, matrix, 0, len(matrix)-1)
        if(idx != -1):
            if(self.binarySearch(target, matrix[idx], 0, len(matrix[idx])-1) == True):
                return True
            else:
                return False
        else:
            return False


class Solution2:
    #Runtime worst case: O(log(n) + log(m)) where n=rows, m=columns, because we do binarySearch on matrix to check which row can be the bound for the target, and then regular binarySearch to check if target exits.
    #I want to say space complexity is also O(log(n) + log(m)) since we're using recursion which adds on memory to stack for each call

    def binarySearchMatrix(self, target, matrix, begin, end):
        if(begin > end):
            return -1
        if (begin == end):
            if matrix[begin][0] <= target and target <= matrix[begin][len(matrix[begin])-1]:
                return begin
            else:
                return -1
            
        mid = (end-begin)//2 + begin
        
        if(matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid])-1]):
            return mid
        
        elif(target < matrix[mid][0]):
            return self.binarySearchMatrix(target, matrix, begin, mid-1)
        elif(target > matrix[mid][len(matrix[mid])-1]):
            
            return self.binarySearchMatrix(target, matrix, mid+1, end)
        
        
        
    def binarySearch(self, target, array, begin, end):
        if begin > end:
            return False
        
        if begin == end:
            if array[begin] == target:
                return True
            else:
                return False
            
        mid = (end-begin)//2 + begin
        
        if(array[mid] == target):
            return True
        
        elif(target < array[mid]):
            return self.binarySearch(target, array, begin, mid-1)
        elif(target > array[mid]):
            return self.binarySearch(target, array, mid+1, end)
        


class Solution: 
    #Worst case is O(n), n=rows.length, m=columns.length (Techincally O(n-1 + log(m)) because if we find the last row is the bound of the target, then we use binary Search to check if target exists in row)

    def binarySearch(self, target, array, begin, end):
        if begin > end:
            return False
        
        if begin == end:
            if array[begin] == target:
                return True
            else:
                return False
            
        mid = (end-begin)//2 + begin
        
        if(array[mid] == target):
            return True
        
        elif(target < array[mid]):
            return self.binarySearch(target, array, begin, mid-1)
        elif(target > array[mid]):
            return self.binarySearch(target, array, mid+1, end)
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(0, len(matrix)):
            if matrix[row][0] <= target and target <= matrix[row][len(matrix[row])-1]:
                if(self.binarySearch(target, matrix[row], 0, len(matrix[row])-1) == True):
                    return True
            
        return False
