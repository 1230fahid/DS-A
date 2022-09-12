class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class queue_ll:
    def __init__(self):
        self.head = None
        self.node = None
    def enqueue(self,value):
        N = Node(value)
        self.node = N
        self.node.next = self.head
        self.head = self.node
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        temp1 = self.node
        temp2 = temp1
        while(temp1.next != None):
            temp2 = temp1
            temp1 = temp1.next
        temp2.next = None
        return temp1.value
    def isEmpty(self):
        if(self.head == None):
            return bool(True)
        else:
            return bool(False)
    def peek(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        return self.head.value
    def printqueue(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        temp = self.head
        while(temp != None):
            print("Queue value is ", temp.value)
            temp = temp.next

class BT:
    def preorderTraversal(self,rootnode): ##Full Time Comp: O(n), Space Comp: O(n)
        if rootnode == None:  ## O(1)
            return ##O(1)
        print(rootnode.val) ##O(1)
        self.preorderTraversal(rootnode.left) ##O(n/2)
        self.preorderTraversal(rootnode.right) ##O(n/2)
    def inorderTraversal(self,rootnode):  #Full Time O(n), Space O(n)
        if rootnode == None:
            return
        print("Here 1, Node is ", rootnode.val)
        self.inorderTraversal(rootnode.left) #O(n/2)
        print(rootnode.val)
        self.inorderTraversal(rootnode.right) #O(n/2)
        print("Here 2, Node is ", rootnode.val)
    def postorderTraversal(self,rootnode):  #Full Time O(n), Space O(n)
        if rootnode == None:
            return
        self.postorderTraversal(rootnode.left) #O(n/2)
        self.postorderTraversal(rootnode.right) #O(n/2)
        print(rootnode.val)
    #def levelorderTraversal(self, rootnode):
    #    if rootnode == None:
    #        return
    #    else:
    #        customQueue = queue_ll()
    #        customQueue.enqueue(rootnode)
    #        while not(customQueue.isEmpty()):
    #            root = customQueue.dequeue()
    #            print(root.val)
    #            if(root.left == None):
    #                customQueue.enqueue(root.left)
    #            if(root.right == None):
    #                customQueue.enqueue(root.right)
    #def insertNode(self, rootnode, newnode):
    #    if rootnode == None:
    #        rootnode = newnode
    #        return
    #    #print(rootnode.val) ##O(1)
    #    self.insertNode(rootnode.left, newnode) ##O(n/2)
    #    self.insertNode(rootnode.right, newnode) ##O(n/2)
        
N1 = TreeNode(1)
N2 = TreeNode(2)
N3 = TreeNode(3)
N4 = TreeNode(4)
N5 = TreeNode(5)
N6 = TreeNode(6)
N7 = TreeNode(7)
N8 = TreeNode(8)
N9 = TreeNode(9)
N10 = TreeNode(10)
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8
N4.right = N9
B1 = BST()
print("Preorder Traversal of B1 is:")
B1.preorderTraversal(N1)
print("\nInorder Traversal of B1 is:")
B1.inorderTraversal(N1)
print("\nPostorder Traversal of B1 is:")
B1.postorderTraversal(N1)
#print("\nLevelorder Traversal of B1 is:")
#B1.levelorderTraversal(N1)
#Insert Node
print("\nInserting node N10 in B1:")
#B1.insertNode(N1, N10)
#B1.preorderTraversal(N1)
