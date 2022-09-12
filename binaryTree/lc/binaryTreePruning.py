# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, arr):
        if(root == None):
            return []
        
        if(root.val == 1):
            arr.append(1)
            #return True
        
        leftarr = []
        rightarr = []
        leftarr = self.dfs(root.left, leftarr)
        rightarr = self.dfs(root.right, rightarr)
        if(len(leftarr) == 0):
            root.left = None
        if(len(rightarr) == 0):
            root.right = None
        arr = arr + leftarr + rightarr
        return arr
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        self.dfs(root, arr)
        if(root.val == 0 and root.right == None and root.left == None):
            root = None
        return root
