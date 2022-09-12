#Problem: Convert singly-linked list to BST

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)
class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if(head == None):
            return None
        root = head
        length = 0
        while(root != None):
            length+=1
            root = root.next
        mid = length//2
        root = head
        i = 0
        prev = head
        after = root.next
        while(i < mid):
            prev = root
            root = root.next
            after = root.next
            i+=1
        troot = TreeNode(root.val)
        root.next = None
        prev.next = None
        if(mid == 0):
            troot.left = self.sortedListToBST(None)
        else:
            troot.left = self.sortedListToBST(head)
        troot.right = self.sortedListToBST(after)
        return troot
# Method 1: Convert linked list to array and then to BST
