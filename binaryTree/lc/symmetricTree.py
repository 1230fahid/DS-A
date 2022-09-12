class Solution:
    def isSymmetric_v1(self, root):
        # Your Code Here
        if root == None:   #initial condition if no nodes
            return True
        return (self.solve(root.left, root.right))
    
    def solve(self,left,right):
        if left == None and right == None:  #if there are no more nodes on either side, then return True
            return True
        if left == None or right == None: #if there is a node on one side, but not the other, return False
            return False
        if left.data != right.data:  #if a node on both sides, but unequal values
            return False

        return (self.solve(left.left,right.right) and self.solve(left.right,right.left))  #returns boolean using an AND. checks the leftmost and rightmost since they would be symmetrical, then the right of the node and the left of the node in the opposite side, since they're symmetrical. If both return True, then that means the subtree is symmetrical.
    
    def isSymmetric_v2(self, root: TreeNode) -> bool:
        if root is None:   #initial condition
            return True 
        stack = [(root, root)] #append root to stack

        while stack:   #checks to make sure stack is not empty
            node1, node2 = stack.pop() #node1=1, node2=1, stack=[] #node1=2, node2=2, stack=[(2,2)]
            if node1 is None and node2 is None:
                pass
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                stack.append((node1.left, node2.right))  #stack=[(2,2)] #stack=[(2,2), (3,4)]
                stack.append((node1.right, node2.left))  #stack=[(2,2), (2,2)] #stack=[(2,2), (3,4), (3,4)]

        return True



#Ex)  [1,2,2,3,3,4,4] 1) self.solve(2,2) which both have values and are equal. 2) self.solve(3, 4) and self.solve(3,4), both have values and are equal. Recursively goes to each Node.

#What do these solutions have in common? Both are traversing the tree, going through each node on each side. v1 uses recursion on both sides (easier to understand). v2 uses a while loop that checks the sides of a subtree, until one side is null, and then goes to the other side of the subtree, and checks it as well (unsure a bit)? Both are looking through each side and checking if anode on one sides exists, but doesnt on the other side, and checks if the values aren't equal, which it Fails in both case.
