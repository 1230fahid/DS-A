# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, start, root, condition, arr):
        if(root == None):
            return
        if(root == condition):
            return start
        if(root.left == condition or root.right == condition):
            arr.append(root)
            return start
        
        
        self.traverse(start, root.left, condition, arr)
        if(len(arr) > 0):
            arr.append(root)
            return
        self.traverse(start, root.right, condition, arr)
        if(len(arr) > 0):
            arr.append(root)
            return
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        arr1 = []
        arr2 = []
        arr3 = []
        con1 = self.traverse(p, p, q, arr1)
        if(len(arr1) != 0):
            return p
        
        con2 = self.traverse(q, q, p, arr2)
        if(len(arr2) != 0):
            return q
        
        
        self.traverse(root, root, p, arr3)
        #print(arr3)
        arr3 = arr3[::-1]
        arr4 = []
        num = 0
        for i in range(0, len(arr3)):
            arr4 = []
            self.traverse(arr3[i], arr3[i], q, arr4)
            if(len(arr4) == 0):
                #return arr3[i-1]
                break
            num+=1
        return arr3[num-1]
