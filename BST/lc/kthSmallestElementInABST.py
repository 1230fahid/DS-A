# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, arr):
        if(root == None):
            return
        arr.append(root.val)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.dfs(root, arr)
        arr.sort()
        return arr[k-1]
