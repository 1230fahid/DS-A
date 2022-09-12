class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left == None:
            rootNode.left = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right == None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return "The node has been successfully inserted"
    #Time O(log(n)), Space O(log(n))

def preOrderTraversal(rootNode):
    if rootNode == None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)
    #Time O(n), Space O(n)

def inOrderTraversal(rootNode):
    if rootNode == None:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if rootNode == None:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)

def preOrder(rootNode):
    stack = []
    stack.append(rootNode)
    tup = ()
    print(rootNode.data)
    while(len(stack) != 0):
        if stack[len(stack) - 1].left != None and stack[len(stack)-1].left.data not in tup:
            stack.append(stack[len(stack)-1].left)
            print(stack[len(stack)-1].data)
        elif stack[len(stack) - 1].right != None and stack[len(stack)-1].right.data not in tup:
            stack.append(stack[len(stack)-1].right)
            print(stack[len(stack)-1].data)
        else:
            tup1 = (stack[len(stack)-1].data,)
            stack.pop()
            tup = tup + tup1

    #Time O(n), Space: O(n)

def inOrder(rootNode):
    stack = []
    stack.append(rootNode)
    tup = ()
    #print(rootNode.data)
    while(len(stack) != 0):
        if stack[len(stack) - 1].left != None and stack[len(stack)-1].left.data not in tup:
            stack.append(stack[len(stack)-1].left)
            #print(stack[len(stack)-1].data)
        elif stack[len(stack) - 1].right != None and stack[len(stack)-1].right.data not in tup:
            stack.append(stack[len(stack)-1].right)
            #print(stack[len(stack)-1].data)
        else:
        #elif stack[len(stack)-1].data not in tup:
            tup += (stack[len(stack)-1].data,)
            print(stack[len(stack)-1].data)
            stack.pop()
            if(len(stack) != 0): 
                if (stack[len(stack)-1].data not in tup):
                    print(stack[len(stack)-1].data)
                    tup += (stack[len(stack)-1].data,)
                else:
                    stack.pop()
                    if(stack[len(stack)-1].data == rootNode.data) and (stack[len(stack)-1].data in tup):
                        break
                    print(stack[len(stack)-1].data)
                    tup += (stack[len(stack)-1].data,)
            

            #tup = tup + tup1

    #Time O(n), Space: O(n)


def levelOrderTraversal(rootNode):
    if rootNode == None:
        return
    else:
        queue = []
        queue.append(rootNode)
        while(len(queue) != 0):
            root = queue.pop(0)
            print(root.data)
            if(root.left != None):
                queue.append(root.left)
            if(root.right != None):
                queue.append(root.right)

def main():
    newBST = BSTNode(None)  #Time O(1), Space O(1)
    print(insertNode(newBST, 70))
    print(insertNode(newBST, 50))
    print(insertNode(newBST, 90))
    print(insertNode(newBST, 30))
    print(insertNode(newBST, 60))
    print(insertNode(newBST, 80))
    print(insertNode(newBST, 100))
    print(insertNode(newBST, 20))
    print(insertNode(newBST, 40))
    print(insertNode(newBST, 95))
    print(insertNode(newBST, 110))
    print("My preorder traversal:")
    preOrder(newBST)
    print("\nOther preorder traversal:")
    preOrderTraversal(newBST)
    print("\nMy inorder traversal:")
    inOrder(newBST)
    print("\nOther inorder traversal:")
    inOrderTraversal(newBST)
    print("\nOther postorder traversal:")
    postOrderTraversal(newBST)
    print("\nLevel Order Traversal is:")
    levelOrderTraversal(newBST)

if __name__ == "__main__":
    main()
