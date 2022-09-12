class Graph:
    def __init__(self):
        self.graph = {}

    #Function add an edge to the graph
    def addEdge(self, u, v):
        if(u not in self.graph.keys()):
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    #Function to print a BFS of graph
    def BFS(self, s):
        #Mark all vertices as not visited
        visited = [False] * (max(self.graph)+1)

        #Create a queue for BFS
        queue = []

        #Mark the source node as
        #visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            #Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            #Get all adjacent vertices of the dequeued vertex s. If an adjacent
            #has not been visited, then mark it
            #visited and enqueue it
            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is BFS Traversal (starting for vertex 2)")

g.BFS(2)
