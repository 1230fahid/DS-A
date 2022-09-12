# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recurse(self, head, length):
        if(length == 0):
            return head
        if(length == 1):
            return head.next 
        m = self.recurse(head.next, length-2)
        if(m == False):
            return False
        if(head.val == m.val):
            if(m.next == None):
                return True
            return m.next
        return False
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next) == None:
            return True
        node = head
        length = 0
        while(node != None):
            length += 1
            node=node.next
        
        return self.recurse(head, length)
        
