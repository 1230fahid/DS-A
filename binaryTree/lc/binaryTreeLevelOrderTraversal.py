# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        arr = []
        mydict = {}
        queue = [root]
        level = 0
        mydict[root] = [root.val, level]
        finalLevel = level
        
        while(len(queue) != 0):
            node = queue.pop(0)
            if(node in mydict.keys()):
                level = mydict[node][1]
                finalLevel = level
            if(node.left != None):
                mydict[node.left] = [node.left.val, level+1]
                queue.append(node.left)
            if(node.right != None):
                mydict[node.right] = [node.right.val, level+1]
                queue.append(node.right)
        
        
        for i in range(0, finalLevel+1):
            arr.append([])
            for key in mydict.keys():
                if(mydict[key][1] == i):
                    arr[len(arr)-1].append(mydict[key][0])
        
        return arr
