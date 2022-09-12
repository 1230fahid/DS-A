# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, depth, mydict):
        if(root == None):
            return
        mydict[depth] = root.val
        #arr.append(root.val)
        self.traverse(root.left, depth+1, mydict)
        self.traverse(root.right, depth+1, mydict)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mydict = {}
        arr = []
        self.traverse(root, 1, mydict)
        #print(mydict)
        for i in mydict.values():
            arr.append(i)
        return arr
