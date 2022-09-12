class Solution:
    def merge(self, matrix):
        if(len(matrix) == 0):
            return []
        if(len(matrix) == 1):
            return matrix[0]
        matrix=self.merge(matrix[0:len(matrix)//2]) + self.merge(matrix[len(matrix)//2:len(matrix)])
        matrix.sort()
        return matrix
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix=self.merge(matrix)
        return matrix[k-1]
