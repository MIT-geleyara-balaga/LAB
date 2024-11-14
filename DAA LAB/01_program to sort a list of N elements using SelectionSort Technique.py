def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

try:
    N=int(input("Enter the NUmber of elements in the list : "))
    arr=[]
    for i in range(N):
        element=int(input(f"Enter the Element {i+1} : "))
        arr.append(element)

    print("Original List : ",arr)
    selection_sort(arr)
    print("Sorted List : ",arr)

except ValueError:
    print("Please enter a valid number of elments and valid elements for the list.")