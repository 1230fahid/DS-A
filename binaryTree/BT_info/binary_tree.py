class BinaryTree:
    def __init__(self, size):
        self.maxSize = size;
        self.customList = size * [None]
        self.lastUsedIndex = 0
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:  #Time: O(1)
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value #Time: O(1)
        self.lastUsedIndex += 1 #Time: O(1)
        return "The Value has been successfully inserted"
        #Total Time O(1), Total Space O(1)
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)): #Time O(n), Space O(1)
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
        #Total Time O(n)(recursion for each preOrder), Space O(n) (memory inserted into stack)
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
        #Total Time O(n), Space O(n)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
        #Total Time O(n), Space O(n)

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
        #Total Time O(n), Space O(1)
newBT = BinaryTree(8)   ## Time: O(1) because just using two variables, Space: O(n) because making n-size list
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.searchNode("Tea"))
print(newBT.searchNode("Hot"))
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
print("Beginning of Pre Order Traversal")
newBT.preOrderTraversal(1)
print("\nBeginning of In Order Traversal")
newBT.inOrderTraversal(1)
print("\nBeginning of Post Order Traversal")
newBT.postOrderTraversal(1)
print("\nBeginning of Level Order Traversal")
newBT.levelOrderTraversal(1)
