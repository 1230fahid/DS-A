# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max(self, root, arr, depth):
        if(root == None):
            return
        #print(root.val)
        depth += 1
        arr.append(depth)
        self.max(root.left, arr, depth)
        #print(root.val)
        self.max(root.right, arr, depth)
        #print(root.val)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        arr = [0]
        depth = 0
        self.max(root, arr, depth)
        return max(arr)
    
