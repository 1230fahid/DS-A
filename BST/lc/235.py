# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root != None:
            if(p.val < root.val and q.val < root.val):
                root = root.left
            elif(p.val > root.val and q.val > root.val):
                root = root.right
            elif(p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root
            elif((p.val == root.val) and (q.val > root.val)) or ((p.val == root.val) and (q.val < root.val)):
                return p
            elif(q.val == root.val and p.val > root.val) or (q.val == root.val and p.val < root.val):
                return q        

################################################################################
# Task:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

################################################################################
# (Solution developed with help from GeeksforGeeks)
# Time: Unknown, definitely more than 30 minutes. 
# What can I learn here?
# Don't always need to use recursion to traverse BST
# If comparing nodes to BST, check if values are greater or less than BST, and traverse like that.
