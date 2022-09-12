#need to optimize

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = []
        node = head
        length = 0
        for i in range(0, m):
            matrix.append([])
            for j in range(0,n):
                matrix[i].append(None)
        i = 0
        j = 0
        prev = None
        
        while node != None:
            length +=1
            prev = node
            node = node.next
        
        store = m*n - length
        while(store != 0):
            prev.next = ListNode(-1)
            prev = prev.next
            store -= 1
        
        prev.next = None
    
        beginm = 0
        beginn = 0
        
        node = head
        
        rows = m
        cols = n
        self.spiral(0, beginm, beginn, m, n, node, matrix, rows, cols)
        #print(matrix)
        return matrix
    
    def spiral(self, cnt, beginm, beginn, m, n, head, matrix, rows, cols):
        #print(matrix)
        
        if(cnt > rows*cols):
            return
        
        i = beginm
        j = beginn
        
        while(j != n):
            if(cnt > rows*cols):
                return
            if(head != None):
                matrix[i][j] = head.val
                head = head.next
            else:
                matrix[i][j] = -1
            cnt += 1
            j += 1
            #head = head.next
        j -= 1
        if(cnt > rows*cols):
            return
        #if(head == None):
        #    return
        
        i+=1
        while(i != m):
            if(cnt > rows*cols):
                return
            if(head != None):
                matrix[i][j] = head.val
                head = head.next
            else:
                matrix[i][j] = -1
            #matrix[i][j] = head.val
            cnt+=1
            i += 1
            #head = head.next
        i-=1
        if(cnt > rows*cols):
            return
        #if(head == None):
        #    return
        
        j -= 1
        endn = beginn
        while(j != endn-1):
            if(cnt > rows*cols):
                return
            if(head != None):
                matrix[i][j] = head.val
                head = head.next
            else:
                matrix[i][j] = -1
            #matrix[i][j] = head.val
            cnt+=1
            j-=1
            #head = head.next
        
        j += 1    
        
        endm = beginm
        i-=1
        while(i != endm):
            if(cnt > rows*cols):
                return
            if(head != None):
                matrix[i][j] = head.val
                head = head.next
            else:
                matrix[i][j] = -1
            #matrix[i][j] = head.val
            cnt+=1
            i-=1
        
        self.spiral(cnt, beginm+1, beginn+1, m-1, n-1, head, matrix, rows, cols)
