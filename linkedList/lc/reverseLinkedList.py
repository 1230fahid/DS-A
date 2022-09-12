# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        
        prev = head
        node = head
        last = None
        while(node != None):
            if(prev == node):
                node = node.next
                if(node == None):
                    break
                prev.next = last
                last = prev
                prev = node
            #store = node.next.val
            
            
            
        return prev
