def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

try:
    N=int(input("Enter the number of elements in the list : "))
    arr=[]
    for i in range(N):
        element=int(input(f"Enter the Element {i+1} : "))
        arr.append(element)

    print("Original List : ",arr)
    selection_sort(arr)
    print("Sorted List : ",arr)

except ValueError:
    print("Please enter a valid number of elments and valid elements for the list.")


"""
:OUTPUT:
Enter the number of elements in the list : 5
Enter the Element 1 : 9
Enter the Element 2 : 99
Enter the Element 3 : 1  
Enter the Element 4 : 44
Enter the Element 5 : 18
Original List :  [9, 99, 1, 44, 18]
Sorted List :  [1, 9, 18, 44, 99]

"""