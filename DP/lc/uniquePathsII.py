class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0] == 1):
            return 0
        #path = [[]]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        reached = 0
        self.traverse(0, 0, obstacleGrid, reached, len(obstacleGrid[0])-1, len(obstacleGrid)-1)
        return obstacleGrid[0][0]

    def traverse(self, x, y, obstacleGrid, reached, finalX, finalY):
        if x == len(obstacleGrid[0]) or y == len(obstacleGrid):
            return 0
        elif obstacleGrid[y][x] == -1:
            return 0
        elif x == finalX and y == finalY:
            reached += 1
            obstacleGrid[y][x] = reached
        elif(obstacleGrid[y][x] == 0):
            obstacleGrid[y][x] = self.traverse(x, y+1, obstacleGrid, reached, finalX, finalY) + self.traverse(x+1, y, obstacleGrid, reached, finalX, finalY)
        return obstacleGrid[y][x]
