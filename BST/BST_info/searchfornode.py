class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchfornode(node, root):  #Time O(log(n)), Space o(log(n))
    if(root == None):
        print("Not found")
        return
    if(node.val == root.val):
        print("Node found")
        return
    elif(node.val < root.val):
        root = root.left
    elif(node.val > root.val):
        root = root.right
    searchfornode(node, root)
    
    
    



Root = TreeNode(10)
Left1 = TreeNode(5)
Right1 = TreeNode(15)
Root.left = Left1
Root.right = Right1
Left2 = TreeNode(2)
Right2 = TreeNode(6)
Left1.left = Left2
Left1.right = Right2
Left3 = TreeNode(12)
Right3 = TreeNode(16)
Right1.left = Left3
Right1.right = Right3

N1 = TreeNode(1)

searchfornode(Right3, Root)
searchfornode(N1, Root)
