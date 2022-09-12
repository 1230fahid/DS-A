# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, node, root):
        if(node != None and root == None):
            return False
        if(node.val != root.val):
            return False
        else:
            if(node.next == None):
                return True
        
        if(self.same(node.next, root.left) == True):
            return True
        
        if(self.same(node.next, root.right) == True):
            return True
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if (root == None):
            return False
        
        if(root.val == head.val):
            if(self.same(head, root) == True):
                return True
        
        if(self.isSubPath(head, root.left) == True):
            return True
        if(self.isSubPath(head, root.right) == True):
            return True
        return False
