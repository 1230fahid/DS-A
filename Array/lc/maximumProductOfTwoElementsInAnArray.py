class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root):
        queue = []
        queue.append(root)
        while(len(queue) != 0):
            node = queue.pop(0)
            #print(node.val)
            if(node.left != None):
                queue.append(node.left)
            if(node.right != None):
                queue.append(node.right)
        
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        arr = nums[::-1]
        arr.insert(0, None)
        root = TreeNode(arr[1]) #get root of tree. We know always at least 1 node, so it's fine
        nodes = [None] #placeholder, since we want to start at index 1
        nodes.append(root) #add root at index 1, so we can later on access it and find it's children value
        for i in range(1, len(arr)):
            node = nodes[i] #get ith node.
            if(i*2 >= len(arr)):
                break
            node.left = TreeNode(arr[i*2])
            nodes.append(node.left) #append it's left child
            if(i*2 + 1 >= len(arr)):
                break
            node.right = TreeNode(arr[i*2 + 1])
            nodes.append(node.right) #append it's right child
        
        #self.levelOrder(root) #print out values in each level
        return (root.val-1) * (root.left.val-1)
    
    #this was just a max heap example


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[len(nums)-1]-1) * (nums[len(nums)-2]-1)
