from  collections import deque,defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adjLists=defaultdict(list)
        self.adj=[deque() for _ in range(vertices)]
        self.visited=[False]*vertices

    def add_edge(self,v,w):
        self.adj[v].append(w)
        self.adjLists[v].append(w)

    def bfs(self,s):
        visited=[False]*self.vertices
        queue=deque()
        visited[s]=True
        queue.append(s)
        print("Following is Breadth First Traversal (Starting from vertex{}) : ".format(s))

        while queue:
            s=queue.popleft()
            print(s,end=" ")

            for n in self.adj[s]:
                if not visited[n]:
                    visited[n]=True
                    queue.append(n)

        print()

    def dfs(self,vertex):
        self.visited=[False]*self.vertices
        print("Following is Depth First Traversal (starting from vertex{}) : ".format(vertex))
        self._dfs_recursive(vertex)
        print()

    def _dfs_recursive(self,vertex):
        self.visited[vertex]=True
        print(vertex,end=" ")

        for adj in self.adjLists[vertex]:
            if not self.visited[adj]:
                self._dfs_recursive(adj)

if __name__=="__main__":
    g=Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(0,3)
    g.add_edge(1,2)
    g.add_edge(2,4)

    g.bfs(0)
    g.dfs(0)