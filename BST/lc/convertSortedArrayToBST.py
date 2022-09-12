#Problem: Convert sorted array to BST



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root
    #First the middle is gotten. You want it to be a BST, so it makes sense to get the middle. Why?
    # Because if you keep getting the middle, there will always be a value bigger and smaller than it,
    # and you will assign those values to the left and right of the node. This way you will keep getting a root node
    # that will be the parent of every subtree and will look for values smaller than it to put to the left, and values bigger
    # than it to assign it to right child. Then those nodes will repeat and look for the same thing, which assigns the values
    # correctly and uses the minimum depth and number of nodes needed to make the tree.
#########################################################################################################################################
#Ex 1) [0,1,2,3,4,5]
# 1st loop
# Get the middle => root = TreeNode(3)
# root.left = self.sortedArrayToBST([0,1,2])
## 2nd loop:
## root = TreeNode(1)
## root.left = self.sortedArrayToBST([0])
### 3rd loop:
### root = TreeNode(0)
### root.left = self.sortedArrayToBST(None)
#### 4th loop:
#### nums == None => return None => the previous loop's root.left = None/TreeNode(0).left = None
### Pop this current loop, go back to Loop 3, where TreeNode(0) is created, and go to next statement
### 3rd loop (revisited):
### root.right = self.sortedArrayToBST(None)
#### New 4th loop:
#### nums == None => return None => the previous loop's root.right = None/TreeNode(0).right = None
### Pop this current loop, back to Loop 3, where TreeNode(0) was created, and go to next statement
### 3rd loop(revisited):
### return root
## Since root is returned, stack memory pops of this loop and goes back to second loop, where TreeNode(1) was created and go next
## 2nd loop (revisited):
## root.right = self.sortedArrayToBST([2])
### New 3rd loop:
### root = TreeNode(2)
### root.left self.sortedArrayToBST(None)
### Just like before, that will return None, and will pop back to the loop where TreeNode(2) created, making TreeNode(2).left = None
### root.right = self.sortedArrayToBST(None)
### Like two statement before, goes back to loop with TreeNode(2), and TreeNode(2).right = None, goes to next statement
### return root
## Popped and goes back to original second loop, where TreeNode(1).right = TreeNode(2)
## return root
# Goes to 1st loop now
# TreeNode(3).left = TreeNode(1)
# root.right = self.sortedArrayToBST([4,5])
## New 2nd loop:
## root = TreeNode(5)
## root.left = self.sortedArrayToBST([4])
### New 3rd loop:
### root = TreeNode(4)
### root.left = self.sortedArrayToBST(None)
#### New 4th loop:
#### nums == None => return None
### Go back to 3rd loop, where now TreeNode(4).left = None, and next statement
### root.right = self.sortedArrayToBST(None)
#### New 4th loop:
#### nums == None => return None
### Go back to third loop, where now TreeNode(4).right = None and next statement
### return root
## Go back to second loop now, where TreeNode(5).left = TreeNode(4), and go to next statement
## root.right = self.sortedArrayToBST(None)
### New third loop
### nums == None => return None
## Go back to second loop, where now, TreeNode(5).right = None, then go to next statement
## return root
# Now TreeNode(3), the original root, now has TreeNode(3).right = TreeNode(5). Now go to next statement
# returns root, which is the top of the whole tree now

# TreeNode(3) now popped off, stack empty, done
#########################################################################################################################################

    #I'm noticing a lot of binary tree and BST can be solved using recursion most of the time, but you need to use recursion in a
    # way it makes sense for the problem.


def main():
    arr1 = [0,1,2,3,4,5]
    sol = Solution()
    r = sol.sortedArrayToBST(arr1)
    print(r.val)

if __name__ == "__main__":
    main()
