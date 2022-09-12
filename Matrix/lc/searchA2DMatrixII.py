class Solution:
    def binarySearch(self, target, array, begin, end):
        if(begin > end):
            return False
        
        if(begin == end):
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
        for level in range(len(matrix)):
            if matrix[level][0] <= target and target <= matrix[level][len(matrix[level])-1]:
                if(self.binarySearch(target, matrix[level], 0, len(matrix[level])-1) == True):
                    return True
            
        return False
        
