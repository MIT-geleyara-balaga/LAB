def create_directed_graph(vertices,edges):
    graph=[[0]*vertices for _ in range(vertices)]

    for _ in range(edges):
        v1,v2=map(int,input("Enter directed edge (form_vertex to_vertex) : ").split())

        if v1<0 or v1>=vertices or v2<0 or v2>=vertices:
            print(f"Invalid edge({v1},{v2}. skipping.")
            continue

        graph[v1][v2]=1

    return graph

def in_degree(graph,vertex):
    return sum(row[vertex] for row in graph)

def out_degree(graph,vertex):
    return sum(graph[vertex])

def print_in_out_degrees(graph,vertices):
    print("\nVertex\tIn-Degree\tOut-Degree")
    for vertex in range(vertices):
        in_degree_val=in_degree(graph,vertex)
        out_degree_val=out_degree(graph,vertex)
        print(f"{vertex}\t\t{in_degree_val}\t\t\t{out_degree_val}")

def print_directed_graph(graph):
    print("\nDirected Adjacency Matrix : ")
    for row in graph:
        print(" ".join(map(str,row)))

def main():
    vertices=int(input("Enter the number of vertiuces :"))
    edges=int(input("Enter the number of directed edges : "))

    if vertices<=0 or edges<0 or edges>vertices*(vertices-1):
        print("Invalid input.Exiting....")
        return
    
    directed_graph=create_directed_graph(vertices,edges)
    print_directed_graph(directed_graph)
    print_in_out_degrees(directed_graph,vertices)

if __name__=="__main__":
    main()


"""

:OUTPUT:

Enter the number of vertiuces :4
Enter the number of directed edges : 4
Enter directed edge (form_vertex to_vertex) : 0 2
Enter directed edge (form_vertex to_vertex) : 2 3
Enter directed edge (form_vertex to_vertex) : 3 1
Enter directed edge (form_vertex to_vertex) : 1 0

Directed Adjacency Matrix :
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

Vertex  In-Degree       Out-Degree
0               1                       1
1               1                       1
2               1                       1
3               1                       1

"""