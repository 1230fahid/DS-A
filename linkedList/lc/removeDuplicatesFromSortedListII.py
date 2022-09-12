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
        dups = {}
        node = node.next
        while(node != None):
            if(node.val in mydict.keys()):
                dups[node.val] = 0
                erase = node
                prev.next = erase.next
                node = node.next
                erase.next = None
            else:
                mydict[node.val] = 0
                node = node.next
                prev = prev.next
        
        #print(dups)
        if(head.val in dups.keys()):
            head = head.next
        if(head == None):
            return head
        node = head.next
        prev = head
        
        while(node != None):
            if(node.val in dups.keys()):
                prev.next = node.next
                erase = node
                node = node.next
                erase.next = None
            else:
                node = node.next
                prev = prev.next
        if(head.val in dups.keys()):
            head = head.next
        
        return head
