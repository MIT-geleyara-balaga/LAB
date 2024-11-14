import itertools

cities={}

while True:
    city_name=input("Enter the city name (or 'done' to finish) : ").strip()
    if city_name.lower()=='done':
        break
    x,y=map(float,input("Enter the co-ordinates (x,y) :").split())
    cities[city_name]=(x,y)

def distance(city1,city2):
    x1,y1=cities[city1]
    x2,y2=cities[city2]
    return((x1-x2)**2+(y1-y2)**2)**0.5

shortest_route=None
min_distance=float('inf')

for route in itertools.permutations(cities.keys()):
    total_distance=sum(distance(route[i],route[i+1]) for i in range(len(route)-1))
    total_distance+=distance(route[-1],route[0])
    if total_distance<min_distance:
        min_distance=total_distance
        shortest_route=route

print("Shortest Route : ",shortest_route)
print("Shortest Distance : ",min_distance)