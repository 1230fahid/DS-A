# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        if(head1 == None and head2 == None):
            return None
        elif(head1 == None):
            return head2
        elif(head2 == None):
            return head1
        node = None
        if(head1.val <= head2.val):
            node=head1
            head1=head1.next
        else:
            node=head2
            head2=head2.next
        root=node
        while(head1 != None and head2 != None):
            if(head1.val <= head2.val):
                node.next = head1
                head1=head1.next
            else:
                node.next = head2
                head2=head2.next
            node=node.next
        
        if(head1):
            node.next=head1
            
        if(head2):
            node.next=head2
        return root
            
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists) == 0):
            return None
        if(len(lists) == 1):
            return lists[0]
        return self.merge(self.mergeKLists(lists[0:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:len(lists)]))
