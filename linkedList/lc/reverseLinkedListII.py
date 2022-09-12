# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(left == right):
            return head
        prev = head
        node = head
        num = 1
        nextnode = None
        arr = []
        start = None
        while(node != None):
            if(num == left):
                if(prev != head):
                    prev.next = None
                #nextnode = node.next
                start = node
                break
            else:
                if(num != 1):
                    prev = prev.next
                node = node.next
                num += 1
        #num+=1
        while(node != None):
            if(num == right):
                nextnode = node.next
                node.next = None
                break
            else:
                node = node.next
                num += 1
        
        node = start
        while(node != None):
            arr.append(node.val)
            node = node.next
        
        arr = arr[::-1]
        
        newstart = ListNode(arr[0])
        rvs = newstart
        for i in range(1, len(arr)):
            rvs.next = ListNode(arr[i])
            rvs = rvs.next
        
        if(left != 1):
            prev.next = newstart
        else:
            head = newstart
        rvs.next = nextnode

        return head
