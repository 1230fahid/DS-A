"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(node == None):
            return None
        visited = {} ##dictionary to keep track
        node1 = self.routeHelper(node, visited) #get new node back
        return node1
        
    def routeHelper(self, node, visited):
        if(node.val in visited.keys()): #if there's a node that already exists with the same value then just return that node
            return visited[node.val]
        if(len(node.neighbors) == 0): ##if no neighbors, or nodes after current node, then return new node with the same value and add to dictionary
            node1 = Node(node.val)
            visited[node1.val] = node1
            #print(visited)
            return node1
        node1 = Node(node.val)
        visited[node1.val] = node1
        for i in range(0, len(node.neighbors)): #add new nodes to neighbors. This traverses each neighbor array for each node and returns a new node at the end that has all the same values but new memory locations
            node1.neighbors.append(self.routeHelper(node.neighbors[i], visited))
        return node1
        
        ##For this, I basically used DFS. I dont know why I struggled so much before. Just simple dfs recursion and keeping track of nodes already visited
