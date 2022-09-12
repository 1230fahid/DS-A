# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None or k == 0):
            return head
        
        length = 0
        ll = []
        node = head
        while node != None:
            length+=1
            ll.append(node.val)
            node = node.next
        if(k == len(ll)):
            return head
        elif(k > len(ll)):
            rem = k%len(ll)
            for i in range(0, rem):
                num = ll.pop()
                ll.insert(0, num)
            newhead = ListNode(ll[0])
            node = newhead
            for i in range(1, len(ll)):
                node.next = ListNode(ll[i])
                node = node.next
            return newhead
            
            #print(rem)
        else:
            for i in range(0, k):
                num = ll.pop()
                ll.insert(0, num)
        
        #print(ll)
            newhead = ListNode(ll[0])
            node = newhead
            for i in range(1, len(ll)):
                node.next = ListNode(ll[i])
                node = node.next
            return newhead
