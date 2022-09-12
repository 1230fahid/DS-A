# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        node = head
        while node != None:
            i += 1
            node = node.next
        if(i == n):
            return head.next
        elif(n == 1):
            node = head
            prev = None
            while node.next != None:
                prev = node
                node = node.next
            prev.next = None
            return head
        else:
            node = head
            prev = None
            for j in range(0, i-n):
                prev = node
                node = node.next
            prev.next = node.next
            node.next = None
            return head
