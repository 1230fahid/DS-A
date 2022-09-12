class Solution:
    def island(self, grid, row, col, traversed):
        #Here I just use DFS until I reach a point where all the surrounding indexes are either ones I've already traversed, or are all 0's. At that point if all 0's or/and all 0's surrounding and I've already traversed, then I can return since it's an island
        if(row in traversed.keys()):
            if(col in traversed[row]):
                return
            else:
                traversed[row].append(col)
        else:
            traversed[row] = [col]
            
            
        if(row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[row])):
            return
        

        if(row-1 >= 0 and grid[row-1][col] == '1'):
            self.island(grid, row-1, col, traversed)
        

        if(row + 1 < len(grid) and grid[row+1][col] == '1'):
            self.island(grid, row+1, col, traversed)
        

        if(col-1 >= 0 and grid[row][col-1] == '1'):
            self.island(grid, row, col-1, traversed)
        

        if(col + 1 < len(grid[row]) and grid[row][col+1] == '1'):
            self.island(grid, row, col+1, traversed)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        traversed = {}                        
        num = 0
        
        #used dictionary traversed for memoization, to check if I already traversed a land that was part of a previous island, because I only want new islands, not ones I've already been at
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    if(len(traversed) == 0 or i not in traversed.keys() or j not in traversed[i]): 
                        self.island(grid, i, j, traversed)
                        num += 1
                        #oneDict = {}         
                        
        return num
