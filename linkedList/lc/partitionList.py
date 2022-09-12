# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        node = head
        less = []
        greater = []
        while(node != None):
            if(node.val < x):
                less.append(node)
            else:
                greater.append(node)
            node = node.next
        
        head = ListNode()
        newnode = ListNode()
        if(len(less) != 0):
            #newnode = less[0]
            head.next = less[0]
            newnode = head.next
            #print("newnode.val is %d" % (newnode.val))
            i = 1
            while i < len(less):
                newnode.next = less[i]
                i+=1
                newnode=newnode.next
                #print("newnode.val is %d" % (newnode.val))
        if(len(greater) != 0):
            if(len(less) == 0):
                #newnode = greater[0]
                head.next = greater[0]
                newnode = head.next
            else:
                newnode.next = greater[0]
                newnode=newnode.next
            #print("newnode.val is %d" % (newnode.val))
            i=1
            while i < len(greater):
                newnode.next = greater[i]
                i+=1
                newnode=newnode.next
                #print("newnode.val is %d" % (newnode.val))
        newnode.next = None
        #print("head.next.val is ", head.next.val)
        return head.next

