class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[]]
        for i in range(0, m):
            for j in range(0, n):
                path[i].append(0)
            path.append([])
        path.pop()
        reached = 0
        self.traverse(path, 0, 0, reached, n-1, m-1)
        return path[0][0]

    def traverse(self, path, x, y, reached, finalX, finalY):
        if x == len(path[0]) or y == len(path):
            return 0
        elif x == finalX and y == finalY:
            reached += 1
            path[y][x] = reached
        elif(path[y][x] == 0):
            path[y][x] = self.traverse(path, x, y+1, reached, finalX, finalY) + self.traverse(path, x+1, y, reached, finalX, finalY)
        return path[y][x]
    
    #What I did here was I used memoization (top-down recursion) and first traversed all the way until I found one path, and then stored it to the array, so that when the stack pops that memory and goes back one stack before the first traversal. Here, it adds how many paths are found when it touches the cooridnate that lead to the first traversal completing i.e.) (6,0) -> (6,1) -> (6,2) is one unique path. Then pop back and (5,0) checks (5,1) and (6,0). It knows (6,0) already has 1 unique path, now that is added to how many paths are found in (5,1) and stores it in the array at location [5,0], which results path[5,0] = 3. Then path[4,0] is the sum of path[4,1] and path[5,0]=3 and so on. This gets all the way back to path[0,0] which is the sum of all of the unique paths. Also look at graph paper work. 
