# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None and list2 == None):
            return None
        if(list1==None):
            return list2
        if(list2==None):
            return list1
        list3=None
        node1=list1
        node2=list2
        if(list1.val < list2.val):
            list3 = list1
            node1=node1.next
        else:
            list3 = list2
            node2=node2.next
        node3=list3
        while(node1!=None and node2!=None):
            if(node1.val < node2.val):
                node3.next = node1
                node1=node1.next
            else:
                node3.next = node2
                node2=node2.next
            node3=node3.next
        #while(node1!=None):
        if(node1):
            node3.next = node1
         #   node3=node3.next
          #  node1=node1.next
        
        #while(node2!=None):
        if(node2):
            node3.next = node2
         #   node3=node3.next
          #  node2=node2.next
        
        while(list1!=None):
            print("list1 currently is ", list1)
            list1=list1.next
        while(list2!=None):
            print("list1 currently is ", list2)
            list2=list2.next
        
        return list3
