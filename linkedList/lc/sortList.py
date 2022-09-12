# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_lists(self, head1, head2):
        root = None
        nxt1=None
        nxt2=None
        head = None
        if(head1.val < head2.val):
            head=head1
            root=head1
            head1=head1.next
        else:
            head=head2
            root=head2
            head2=head2.next
        #print("Root is ", root)
        while(head1 != None and head2!=None):
            if(head1.val < head2.val):
                root.next=head1
                head1=head1.next
            else:
                root.next=head2
                head2=head2.next
            root=root.next
            root.next=None

        if(head2!=None):
            root.next=head2
            #root=root.next
        elif(head1!=None):
            root.next=head1
            #root=root.next
        root=head
        #print(root)
        return root
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
        left = head
        new_left=self.sortList(left)
        new_node=self.sortList(node)
        return self.merge_lists(new_left, new_node)
