# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_lists(self, head1, head2):
        root = None
        head = None
        if(head1.val < head2.val):
            root=head1
            head1=head1.next
        else:
            root=head2
            head2=head2.next
        head = root
        while(head1 != None and head2!=None):
            if(head1.val < head2.val):
                root.next=head1
                head1=head1.next
            else:
                root.next=head2
                head2=head2.next
            root=root.next
        if(head2):
            root.next=head2
        elif(head1):
            root.next=head1
        return head
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        if(head.next == None):
            return head
        node = head
        cnt = 0
        while(node != None):
            cnt+=1
            node=node.next
        mid = cnt//2
        left = head
        for i in range(0, mid-1):
            left = left.next
        node = left.next
        left.next = None
        return self.merge_lists(self.sortList(head), self.sortList(node))
