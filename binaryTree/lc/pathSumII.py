# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
        self.arr2 = []
        self.root = None
    def dfs(self, root, targetSum):
        if(root == None):
            return root
        targetSum-=root.val
        self.arr.append(root.val)
        l1=self.dfs(root.left, targetSum)
        r1=self.dfs(root.right, targetSum)
        if(l1 == None and r1 == None):
            if (targetSum == 0):
                arr = self.arr + [None]
                self.arr2.append(arr[0:len(arr)-1:1])
                #print(self.arr2)
        self.arr.pop()
        return root
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if(root == None):
            return []
        self.root = root
        self.dfs(root, targetSum)
        #print(self.arr2)
        return self.arr2
