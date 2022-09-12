# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        
        num = 1
        
        node = head
        prev = node
        newhead = None
        
        while(node != None):
            num += 1
            node = node.next
            if(num == 2):
                nextnode = node.next
                node.next = None
                prev.next = nextnode
                node.next = prev
                newhead = node
        
        newprev = newhead.next
        newnode = newhead.next.next
        if(newnode == None):
            return newhead
        
        newnextnode = newhead.next.next.next
        if(newnextnode == None):
            return newhead
        
        
        #2->1->3->4->5
        #newprev = 1
        #newnode = 3
        #newnextnode = 4
        while(newnode != None):
            newprev.next = None #2->1->None
            nextnode = newnextnode.next #nextnode = 5
            
            newnode.next = nextnode #3->5->None
            newnextnode.next = newnode#4->3
            newprev.next = newnextnode#2->1->4->3->5->None
            #newnode = 3
            #newnextnode = 4
            #newprev = 1
            
            if(nextnode == None or nextnode.next == None):
                break
            else:
                newprev = newprev.next.next
                newnode = newprev.next
                newnextnode = newprev.next.next
        
        return newhead
            
            
            
            
        #walk through example
