# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return head
        mydict = {}
        
        node = head
        prev = head
        mydict[head.val] = 0
        node = node.next
        while(node != None):
            if(node.val in mydict.keys()):
                erase = node
                prev.next = erase.next
                node = node.next
                erase.next = None
            else:
                mydict[node.val] = 0
                node = node.next
                prev = prev.next
            #prev = prev.next
        return head
