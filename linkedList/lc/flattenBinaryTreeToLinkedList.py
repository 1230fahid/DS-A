# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        node1 = root
        node2 = root
        if(node1.left != None):
            node1 = node1.left
        if(node2.right != None):
            node2 = node2.right
        root.left = None
        root.right = None
        print(root)
        print(node1)
        print(node2)
