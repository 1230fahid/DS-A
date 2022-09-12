class Solution:
    def increasing(self, grid, matrix, x, y):
        arr = []
        if((x+1) < len(grid) and grid[x+1][y] > grid[x][y]):
            if (matrix[x+1][y] != 0):
                arr.append(matrix[x+1][y])
            else:
                arr.append(self.increasing(grid, matrix, x+1, y))

        if((y+1) < len(grid[x]) and grid[x][y+1] > grid[x][y]):
            if (matrix[x][y+1] != 0):
                arr.append(matrix[x][y+1])
            else:
                arr.append(self.increasing(grid, matrix, x, y+1))
        
        if((x-1) >= 0 and grid[x-1][y] > grid[x][y]):
            if (matrix[x-1][y] != 0):
                arr.append(matrix[x-1][y])
            else:
                arr.append(self.increasing(grid, matrix, x-1, y))

        if((y-1) >= 0 and grid[x][y-1] > grid[x][y]):
            if(matrix[x][y-1] != 0):
                arr.append(matrix[x][y-1])
            else:
                arr.append(self.increasing(grid, matrix, x, y-1))
        
        if(len(arr) == 0):
            matrix[x][y] = 1
            return 1
        else:
            matrix[x][y] = max(arr)+1
            return matrix[x][y]
        
        
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        matrix = []
        for i in range(0, len(grid)):
            matrix.append([])
            for j in range(0, len(grid[i])):
                matrix[len(matrix)-1].append(0)
                
        maxs = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if(matrix[i][j] == 0):
                    matrix[i][j] = self.increasing(grid, matrix, i, j)
                if(matrix[i][j] > maxs):
                    maxs = matrix[i][j]
                
        
        return maxs
