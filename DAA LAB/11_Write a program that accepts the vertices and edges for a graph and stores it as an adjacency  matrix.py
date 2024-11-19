def create_graph(vertices,edge):
    graph=[[0]*vertices for _ in range(vertices)]

    for _ in range(edge):
        v1,v2=map(int,input("Enter edge (vertex1 vertex2):").split())

        if v1<0 or v1>=vertices or v2<0 or v2>=vertices:
            print(f"Invalid edge ({v1},{v2}. skipping.)")
            continue

        graph[v1][v2]=1
        graph[v2][v1]=1

    return graph

def print_graph(graph):
    print("Adjecency Matrix : ")
    for row in graph:
        print(" ".join(map(str,row)))

def main():
    vertices=int(input("Enter the numbeer of vertices : "))
    edges=int(input("Entere the number of edges : "))

    if vertices<=0 or edges<0 or edges>(vertices*(vertices-1))//2:
        print("Invalid input. Exiting....")
        return
    
    graph=create_graph(vertices,edges)
    print_graph(graph)

if __name__=="__main__":
    main()

"""
:OUTPUT:

Enter the numbeer of vertices : 4
Entere the number of edges : 4
Enter edge (vertex1 vertex2):0 1
Enter edge (vertex1 vertex2):1 2
Enter edge (vertex1 vertex2):2 3
Enter edge (vertex1 vertex2):3 1
Adjecency Matrix : 
0 1 0 0
1 0 1 1
0 1 0 1
0 1 1 0

"""