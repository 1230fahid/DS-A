class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(len(matrix) == 1 and len(matrix[0]) == 1):
            return [matrix[0][0]]
        elif(len(matrix) == 1):
            return matrix[0]
        elif(len(matrix) != 1 and len(matrix[0]) == 1):
            arr = []
            for i in matrix:
                arr.append(i[0])
            return arr        
        
        arr =[]
        
        self.around(arr, matrix, 0, 0, len(matrix), len(matrix[0]))
        #print(arr)
        return arr
        
    def around(self, arr, matrix, beginm, beginn, m, n): #this essentially goes clockwise over a matrix and appends the values, but checks for certain conditions, such as even by even matrix, odd by odd matrix, even by odd matrix, and odd by even matrix
        print(arr)
        if(m - beginm == 0) or (n - beginn == 0): #use or here because if you have a 10 by 2 matrix, the m and beginm will eventually be the same, but the n and beginn won't be, but at that point everything is already traversed so return
            return
        elif(m - beginm) == 1 and (n - beginn) == 1:
            arr.append(matrix[beginm][beginn])
            return
        elif (m - beginm) == 1:
            j = beginn
            while(j != n):
                arr.append(matrix[beginm][j])
                j += 1
            return
        elif (n - beginn) == 1:
            i = beginm
            while(i != m):
                arr.append(matrix[i][beginn])
                i += 1
            return
        
        j = beginn
        i = beginm
        
        while(j != n): ##goes all the way right
            arr.append(matrix[i][j])
            j += 1
        j -= 1 #get back to last column
        
        i += 1 #goes down 1
        while(i != m): #go all the way down
            arr.append(matrix[i][j])
            i += 1
        i -= 1 #get back to last row
        
        j -= 1 #go left one 
        endn = beginn        
        while(j != endn-1): # go all the way left now
            arr.append(matrix[i][j])
            j -= 1
        j+=1
        #print(j)
        i -= 1 #go back up one
        #print(i)
        endm = beginm
        while(i != endm): #go all the way up without reaching starting
            arr.append(matrix[i][j])
            i -= 1
        
        self.around(arr, matrix, beginm + 1, beginn + 1, m-1, n-1) #repeat
