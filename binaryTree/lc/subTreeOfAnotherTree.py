# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtree(self, root, subRoot):
        if(root == None and subRoot == None):
            return True
        elif(root == None and subRoot != None) or (root != None and subRoot == None) or (root.val != subRoot.val):
            return False
        
        return self.subtree(root.left, subRoot.left) and self.subtree(root.right, subRoot.right)
    
    def dfs(self, root, subRoot, arr):
        if(root == None):
            return
        if(root.val == subRoot.val):
            exp = self.subtree(root, subRoot)
            arr[exp] = 1
        self.dfs(root.left, subRoot, arr)
        self.dfs(root.right, subRoot, arr)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr = {}
        arr[False] = 1
        self.dfs(root, subRoot, arr)
        
        if(True in arr.keys()):
            return True
        else:
            return False
