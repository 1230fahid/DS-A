# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if(head.next == None or head.next.next == None):
            return head
        node = head
        n = 0
        while(node != None):
            n+=1
            if(node.next == None):
                break
            else:
                node = node.next.next
        #print(n)
        node = head
        for i in range(1, n):
            node = node.next
        newnode = node.next
        node.next = None
        list1 = []
        while(newnode != None):
            list1.append(newnode.val)
            newnode = newnode.next
        list1 = list1[::-1]
        
        node = head
        i = 0
        while(node.next != None):
            store = node.next
            node.next = ListNode(list1[i])
            i+=1
            node = node.next
            node.next = store
            node = node.next
        
        if(i < len(list1)):
            node.next = ListNode(list1[i])
        #print(head)
