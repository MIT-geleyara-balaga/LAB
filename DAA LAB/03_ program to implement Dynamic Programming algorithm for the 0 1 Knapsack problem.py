def knapsack(weights,values,capacity):
    n=len(weights)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(capacity+1):
            if weights[i-1]>w:
                dp[i][w]=dp[i-1][w]
            else:
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-weights[i-1]]+values[i-1])

    selected_items=[]
    i,w=n,capacity
    while i>0 and w>0:
        if dp[i][w]!=dp[i-1][w]:
            selected_items.append(i-1)
            w-=weights[i-1]
        i-=1

    return dp[n][capacity],selected_items[::-1]

weights=list(map(int,input("Enter the weighjts separated by space : ").split()))
values=list(map(int,input("Enter the calues separated by space : ").split()))
capacity=int(input("Enter Kanpsack capacity : "))

max_value,selected_items=knapsack(weights,values,capacity)

print("MAximum Value : ",max_value)
print("Selected items : ",selected_items)

"""
:OUTPUT:

Enter the weighjts separated by space : 1 2 4 5
Enter the calues separated by space : 5 4 8 6
Enter Kanpsack capacity : 5
MAximum Value :  13
Selected items :  [0, 2]

"""