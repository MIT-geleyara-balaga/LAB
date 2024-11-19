def quick_sort(arr):
    if len(arr)<= 1 :
        return arr
    else:
# Choose the pivot as the last element
        pivot = arr[-1]
        less_than_pivot =[]
        greater_than_pivot =[]

        for x in arr[:-1]:# Exclude the pivot from this loop
            if x <=pivot:
                less_than_pivot.append(x)
            else:
                greater_than_pivot.append(x)
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
try:
    input_list=input( "Enter a list of numbers separated by space:").split()
    input_list= [int(num) for num in input_list]

    if not input_list:
        print("No numbers entered. Please provide a List of numbers. ")
    else:
        sorted_list = quick_sort(input_list)
        print("sorted list using Quick Sort :",sorted_list)
except ValueError:
    print( "Invalid input. Please enter numbers separated by spaceivot")

"""
:OUTPUT:

Enter a list of numbers separated by space:77 12 55 10 2
sorted list using Quick Sort : [2, 10, 12, 55, 77]

"""