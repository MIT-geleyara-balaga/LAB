def find_max_min(arr,low,high):
    if low==high:
        return arr[low],arr[low]
    
    elif high - low==1:
        return max(arr[low],arr[high]),min(arr[low],arr[high])
    
    else:
        mid=(low+high)//2
        max1,min1=find_max_min(arr,low,mid)
        max2,min2=find_max_min(arr,mid+1,high)
        return max(max1,max2),min(min1,min2)
    
arr=list(map(int,input("Enter the elements of the array separated by space : ").split()))

if len(arr)<2:
    print("Array should have at least two elements")
else:
    max_value,min_value=find_max_min(arr,0,len(arr)-1)
    print("Maximum value in the array : ",max_value)
    print("Minimum value in the array : ",min_value)