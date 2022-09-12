class Solution:
    def isSymmetric_v1(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root, root)]
        stack2=[(root.val, root.val)]
        while stack: 
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                pass
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:    
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            
        return True

    def isSymmetric_v2(self, root):
        # Your Code Here
        if root == None:
            return True
        return (self.solve(root.left, root.right))

    def solve(self,left,right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.data != right.data:
            return False

        return (self.solve(left.left,right.right) and self.solve(left.right,right.left))
