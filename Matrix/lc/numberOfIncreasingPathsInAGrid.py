class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        num = 0
        
        newarr = []
        for i in range(0, len(grid)):
            newarr.append([])
            for j in range(0, len(grid[i])):
                newarr[i].append(1)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                self.count(grid, newarr, i, j)
        
                
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                num += newarr[i][j]
        
        return num % (10**9 + 7)
        
    def count(self, grid, newarr, m, n):
        
        if(n+1 >= len(grid[m]) or grid[m][n+1] <= grid[m][n]) and (m+1 >= len(grid) or grid[m+1][n] <= grid[m][n]) and (n-1 < 0 or grid[m][n-1] <= grid[m][n]) and (m-1 < 0 or grid[m-1][n] <= grid[m][n]):
            return 1
        
        if(newarr[m][n] != 1):
            return newarr[m][n]
        
        if(m-1 >= 0 and grid[m-1][n] > grid[m][n]):
            newarr[m][n] += self.count(grid, newarr, m-1, n)
        if(n-1 >= 0 and grid[m][n-1] > grid[m][n]):
            newarr[m][n] += self.count(grid, newarr, m, n-1)
        if(m+1 < len(grid) and grid[m+1][n] > grid[m][n]):
            newarr[m][n] += self.count(grid, newarr, m+1, n)
        if(n+1 < len(grid[m]) and grid[m][n+1] > grid[m][n]):
            newarr[m][n] += self.count(grid, newarr, m, n+1)
        
        return newarr[m][n]
