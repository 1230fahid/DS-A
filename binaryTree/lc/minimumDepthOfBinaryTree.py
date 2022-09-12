# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root, track, arr):
        if(root == None):
            return None
        track+=1
        l1=self.preOrder(root.left, track, arr)
        r1=self.preOrder(root.right, track, arr)
        if(l1 == None and r1 == None):
            arr.append(track)
        return root
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        track=0
        arr = []
        self.preOrder(root, track, arr)
        return min(arr)

