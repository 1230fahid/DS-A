# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, arr, paths):
        arr.append(root.val)
        if((root.left == None) and (root.right == None)):
            #nums = []
            #nums.extend(arr)
            paths.append([])
            for i in arr:
                paths[len(paths)-1].append(i)
            arr.pop()
            return
        
        if(root.left != None):
            self.dfs(root.left, arr, paths)
        
        if(root.right != None):
            self.dfs(root.right, arr, paths)
        
        arr.pop()
            
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if (root == None):
            return
        paths = []
        arr = []
        self.dfs(root, arr, paths)
        
        string = ""
        arr = []
        for path in paths:
            string = ""
            for val in path:
                string = string + str(val) + "->"
            
            arr.append(string[0:len(string)-2])
        
        #print(arr)
        return arr
