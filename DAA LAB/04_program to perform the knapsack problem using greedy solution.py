def knapsack_greedy(values,weights,capacity):
    n=len(values)

    value_per_weight=[(values[i]/weights[i],weights[i],values[i]) for i in range(n)]

    value_per_weight.sort(reverse=True,key=lambda x:x[0])

    total_value=0
    knapsack=[]

    for i in range(n):
        if capacity>=value_per_weight[i][1]:
            knapsack.append((value_per_weight[i][0],value_per_weight[i][1],value_per_weight[i][2]))
            total_value+=value_per_weight[i][2]
            capacity-=value_per_weight[i][1]
        else:
            fraction=capacity/value_per_weight[i][1]
            knapsack.append((value_per_weight[i][0],capacity,value_per_weight[i][0]*capacity))
            total_value+=value_per_weight[i][0]*capacity

        return total_value,knapsack
    
def get_items_data(num_items):
    values=[]
    weight=[]
    for i in range(num_items):
        value=int(input(f"Enter the for item {i+1} : "))
        weight=int(input(f"Enter weight for item{i+1} : "))
        values.append(value)
        weights.append(weight)
    return values,weights

num_items=int(input("Enter the number of items :  "))
values,weights=get_items_data(num_items)
knapsack_capacity=int(input("Enter the knapsack capacity"))

total_value,knapsack_items=knapsack_greedy(values,weights,knapsack_capacity)

print("Total value in the knapscak : ",total_value)
print("Selected items in the knapscak : ",knapsack_items)
