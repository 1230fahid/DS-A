# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root):
        if(root == None):  #Base condition
            return None, []
        
        arr1 = []
        arr2 = []
        leftarr = []
        rightarr = []
        #Here I recommend skipping to line 34, and then coming back to this segment below#
        
        check1, arr1=self.traverse(root.left) #goes down the left child
        if(check1 == True): #Since we know if the leftside was correct or not since we recursed all the way to the bottom and worked out way back up, we can append all of the left child's children node values and check them to see if they're less than the root node's value later on.
            leftarr = leftarr + arr1
        elif(check1 == False): #if our child node had incorrect values on each side of it's binary search tree, than return False, all the way back until we return to wherever the function was originally called, because once we reach one incorrect BST, then the whole thing is completely false. 
            return False,[]
        
        #Same thing as check1, but for right child's children node values
        check2, arr2=self.traverse(root.right) #goes down the right child
        if(check2 == True): 
            rightarr = rightarr + arr2
        elif(check2 == False):
            return False,[]
        
        #################################################################################
        
        if(len(leftarr) == 0 and len(rightarr) == 0): #This occurs when you reach a leaf node
            return True, [root.val] #since no left or right value, no need to compare anything, so you can return it, so that the parent node of this node can compare it's value to this node's value 
        if(len(leftarr) == 0): #Condition for no left nodes but right nodes
            num = 0
            for i in range(0, len(rightarr)): #all child nodes on the right side of a node should always be greater than the current node. Check if this is the case
                if rightarr[i] > root.val:
                    num += 1
            
            if(num == len(rightarr)): #If it's correct, then you return an array, that includes all the values of the children + parent's value
                return True, [root.val] + rightarr
            else:
                return False, [] #else this means there was a node on the rightside of the parentnode, that was less than or equal to the parent, which is wrong since it the nodes must have values GREATER than the parent node
        if(len(rightarr) == 0): #Same thing as previous if statement but opposite
            num = 0
            for i in range(0, len(leftarr)):
                if leftarr[i] < root.val:
                    num += 1
            
            if(num == len(leftarr)):
                return True, [root.val] + leftarr
            else:
                return False, []
        
        #Here we just do both combined, if there are children on both sides of the parent node
        num1 = 0
        for i in range(0, len(rightarr)):
            if rightarr[i] > root.val:
                num1 += 1

        for i in range(0, len(leftarr)):
            if leftarr[i] < root.val:
                num1 += 1
                    
        if(num1!=(len(rightarr) + len(leftarr))):
            return False, []
        else:
            return True, [root.val] + leftarr+rightarr
    
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check, arr = self.traverse(root)
        return check
