#Not my solution. I did solve, but I saw this was a better solution and wanted to understand how it works and what I could learn from it for future level order problems
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: #corner case for no root
            return []
        ret = [] 
        level = 0 #first level will be 0
        pq = deque()
        lOut = []
        pq.append([root,level]) #append the root and level, which in this case is 0. Resulting in pq = [root, 0]
        print("Initial pq is", pq)
        while(len(pq)!=0):
            elem = pq.popleft() #pop from beginning of array
            print("elem is", elem)
            parentLevel = elem[1] #get level
            if(len(ret) < parentLevel): #if we're on a new level, then append the values of the previous level to an array
                ret.append(lOut)
                lOut=[]
            lOut.append(elem[0].val) #appends all values in a level
                
            for child in elem[0].children: #here we need to add the next level to the queue
                pq.append([child,parentLevel+1]) #the child of a node will always be one level below
                print("pq is", pq)
        ret.append(lOut)   
        return ret
