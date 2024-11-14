class UnionFind:
    def __init__(self,size):
        self.parent=list(range(size))

    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            self.parent[root_u]=root_v
            return True
        return False
    
class Graph:
    def __init__(self):
        self.edges=[]

    def add_edge(self,u,v,weight):
        self.edges.append((weight,u,v))

    def kruskal_mst(self):
        self.edges.sort()
        uf=UnionFind(len(self.edges))
        mst_cost=0
        mst_edges=[]

        for weight,u,v in self.edges:
            if uf.union(u,v):
                mst_cost+=weight
                mst_edges.append((u,v,weight))

        return mst_cost,mst_edges
    
if __name__=="__main__":
    g=Graph()

    num_edges=int(input("Enter the number of edges : "))
    for _ in range(num_edges):
        u,v,weight=map(int,input("Enter edge(u v weight): ").split())
        g.add_edge(u,v,weight)

    min_cost,mst_edges=g.kruskal_mst()

    print(f"Minimum Cost of MST : {min_cost}")
    print("Edges in the Minimum Spanning Tree : ")
    for u,v,weight in mst_edges:
        print(f"{u}--{v} (weight: {weight})")