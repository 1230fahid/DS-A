
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(root == None):
            return
        else:
            queue=[]
            queue.append(root)
            head = root
            root.next = None
            while(len(queue) != 0):
                root = queue.pop(0)
                if(root.left != None):
                    root.left.next=root.right
                    queue.append(root.left)
                if(root.right != None):
                    if(root.next!=None):
                        root.right.next=root.next.left
                    else:
                        root.right.next=None
                    queue.append(root.right)
        return head
