# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode((l1.val + l2.val)%10)
        if(l1.val + l2.val >= 10):
            if(l1.next == None):
                l1.next = ListNode(0)
            l1.next.val += 1
        head = root
        l1 = l1.next
        l2 = l2.next
        while(l1 != None and l2 != None):
            head.next = ListNode((l1.val + l2.val)%10)
            if(l1.val + l2.val >= 10):
                if(l1.next == None):
                    l1.next = ListNode(0)
                l1.next.val += 1
            head = head.next
            l1=l1.next
            l2=l2.next
        
        while(l1 != None):
            head.next = ListNode(l1.val%10)
            if(l1.val >= 10):
                if(l1.next == None):
                    l1.next = ListNode(0)
                l1.next.val+=1
            head = head.next
            l1 = l1.next
        while(l2 != None):
            head.next = ListNode(l2.val%10)
            if(l2.val >= 10):
                if(l2.next == None):
                    l2.next = ListNode(0)
                l2.next.val+=1
            head = head.next
            l2 = l2.next
        return root
