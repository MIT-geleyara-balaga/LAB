import heapq

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[] for _ in range(vertices)]

    def add_edge(self,u,v,weight):
        self.graph[u].append((v,weight))
        self.graph[v].append(u,weight)

    def prim_mst(self):
        pq=[(0,0)]
        visited=set()
        min_cost=0

        while pq:
            key,u=heapq.heappop(pq)

            if u in visited:
                continue
            visited.add(u)
            min_cost+=key

            for v,weight in self.graph[u]:
                if v not in visited:
                    heapq.heappush(pq,(weight,v))

        return min_cost
    
if __name__=="__main__":
    num_vertices=int(input("Enter the number of vertices : "))
    g=Graph(num_vertices)

    num_edges=int(input("Enter the number of egdes : "))
    for _ in range(num_edges):
        u,v,weight=map(int,input("Enter edge (u,v weight): ").split())

    min_cost=g.prim_mst()

    print(f"MInimum Cost of MST : {min_cost}")

"""
:OUTPUT:

Enter the number of vertices : 6  
Enter the number of egdes : 9
Enter edge (u,v weight): 0 1 7
Enter edge (u,v weight): 0 2 8
Enter edge (u,v weight): 1 2 3
Enter edge (u,v weight): 2 3 4
Enter edge (u,v weight): 1 3 6
Enter edge (u,v weight): 2 4 3
Enter edge (u,v weight): 3 4 2
Enter edge (u,v weight): 4 5 2
Enter edge (u,v weight): 3 5 5
MInimum Cost of MST : 17

"""