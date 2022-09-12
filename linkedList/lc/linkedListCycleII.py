# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        i = 0
        while head != None:
            if head in nodes.keys():
                return head
            else:
                nodes[head] = i
                i += 1
                head = head.next
        return None
