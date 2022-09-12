class Solution:
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
