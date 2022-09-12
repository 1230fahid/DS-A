# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.bool=False
    def dfs(self, root, targetSum):
        if(root == None):
            return root
        targetSum-=root.val
        l1=self.dfs(root.left, targetSum)
        r1=self.dfs(root.right, targetSum)
        if(l1 == None and r1 == None):
            if(targetSum == 0):
                self.bool=True
        return root
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root == None):
            return False
        self.dfs(root, targetSum)
        return self.bool


class Solution_v2:  #better approach. Don't need helper functions
    def hasPathSum(self, root, targetSum):
        if(root == None):
            return False
        if(root.left == None and root.right == None):
            targetSum-=root.val
            if(targetSum == 0):
                return True
            else:
                return False
        targetSum-=root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
